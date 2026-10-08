package com.dermadesk.app;

import android.Manifest;
import android.annotation.SuppressLint;
import android.content.pm.PackageManager;
import android.speech.RecognizerIntent;
import android.view.WindowManager;
import android.webkit.PermissionRequest;
import android.widget.FrameLayout;
import org.json.JSONObject;
import java.util.ArrayList;
import android.app.Activity;
import android.app.KeyguardManager;
import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.graphics.Color;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.util.Base64;
import android.view.View;
import android.webkit.CookieManager;
import android.webkit.JavascriptInterface;
import android.webkit.ValueCallback;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;

import androidx.core.content.FileProvider;

import java.io.File;
import java.io.FileOutputStream;

/**
 * Derma Desk: the whole app runs inside this screen (no Chrome).
 * The content is the website, so new features and lists arrive without reinstalling;
 * the website's service worker keeps it working offline.
 */
public class MainActivity extends Activity {
    private static final int REQ_FILE = 41, REQ_VOICE = 42, REQ_CAM_CAPTURE = 43, REQ_CAM_LIVE = 44, REQ_UNLOCK = 45;
    private WebView web;
    private View splash;
    private String voiceField;
    private PermissionRequest pendingWebPerm;
    private WebChromeClient.FileChooserParams pendingParams;
    private ValueCallback<Uri[]> fileCallback;
    private Uri cameraUri;

    @SuppressLint({"SetJavaScriptEnabled", "AddJavascriptInterface"})
    @Override
    protected void onCreate(Bundle saved) {
        super.onCreate(saved);
        web = new WebView(this);
        web.setBackgroundColor(Color.parseColor("#14324D"));
        FrameLayout root = new FrameLayout(this);
        root.addView(web, new FrameLayout.LayoutParams(-1, -1));
        View sp = new View(this);
        sp.setBackgroundResource(R.drawable.splash_bg);
        splash = sp;
        root.addView(sp, new FrameLayout.LayoutParams(-1, -1));
        setContentView(root);
        web.postDelayed(this::hideSplash, 8000);

        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true);
        s.setDatabaseEnabled(true);
        s.setAllowFileAccess(false);
        s.setAllowContentAccess(true);
        s.setMediaPlaybackRequiresUserGesture(true);
        s.setLoadWithOverviewMode(true);
        s.setUseWideViewPort(true);
        s.setSupportZoom(false);
        s.setCacheMode(WebSettings.LOAD_DEFAULT);
        s.setUserAgentString(s.getUserAgentString() + " DermaDeskApp/" + BuildConfig.VERSION_NAME);
        CookieManager.getInstance().setAcceptCookie(true);
        CookieManager.getInstance().setAcceptThirdPartyCookies(web, true);

        web.addJavascriptInterface(new Bridge(), "DermaAndroid");

        web.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest req) {
                return handleLink(req.getUrl());
            }

            @Override
            public void onPageFinished(WebView view, String url) {
                view.setBackgroundColor(Color.WHITE);
                view.postDelayed(MainActivity.this::hideSplash, 250);
            }
        });

        web.setWebChromeClient(new WebChromeClient() {
            @Override
            public void onPermissionRequest(PermissionRequest request) {
                runOnUiThread(() -> {
                    boolean wantsCam = false;
                    for (String r : request.getResources()) if (PermissionRequest.RESOURCE_VIDEO_CAPTURE.equals(r)) wantsCam = true;
                    if (!wantsCam) { request.deny(); return; }
                    if (checkSelfPermission(Manifest.permission.CAMERA) == PackageManager.PERMISSION_GRANTED) {
                        request.grant(new String[]{PermissionRequest.RESOURCE_VIDEO_CAPTURE});
                    } else {
                        pendingWebPerm = request;
                        requestPermissions(new String[]{Manifest.permission.CAMERA}, REQ_CAM_LIVE);
                    }
                });
            }

            @Override
            public boolean onShowFileChooser(WebView view, ValueCallback<Uri[]> callback, FileChooserParams params) {
                if (fileCallback != null) fileCallback.onReceiveValue(null);
                fileCallback = callback;
                if (params.isCaptureEnabled() && checkSelfPermission(Manifest.permission.CAMERA) != PackageManager.PERMISSION_GRANTED) {
                    pendingParams = params;
                    requestPermissions(new String[]{Manifest.permission.CAMERA}, REQ_CAM_CAPTURE);
                    return true;
                }
                return launchChooser(params);
            }
        });

        if (saved != null) web.restoreState(saved);
        else web.loadUrl(BuildConfig.APP_URL);
    }

    private void hideSplash() {
        if (splash == null) return;
        final View v = splash; splash = null;
        v.animate().alpha(0f).setDuration(250).withEndAction(() -> ((FrameLayout) v.getParent()).removeView(v)).start();
    }

    private boolean launchChooser(WebChromeClient.FileChooserParams params) {
                try {
                    Intent intent;
                    if (params.isCaptureEnabled()) {
                        File dir = new File(getCacheDir(), "camera");
                        if (!dir.exists()) dir.mkdirs();
                        File photo = new File(dir, "photo_" + System.currentTimeMillis() + ".jpg");
                        cameraUri = FileProvider.getUriForFile(MainActivity.this, "in.dermrx.desk.files", photo);
                        intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                        intent.putExtra(MediaStore.EXTRA_OUTPUT, cameraUri);
                        intent.addFlags(Intent.FLAG_GRANT_WRITE_URI_PERMISSION | Intent.FLAG_GRANT_READ_URI_PERMISSION);
                    } else {
                        cameraUri = null;
                        intent = params.createIntent();
                        if (params.getMode() == WebChromeClient.FileChooserParams.MODE_OPEN_MULTIPLE) intent.putExtra(Intent.EXTRA_ALLOW_MULTIPLE, true);
                    }
                    startActivityForResult(intent, REQ_FILE);
                    return true;
                } catch (Exception e) {
                    if (fileCallback != null) fileCallback.onReceiveValue(null);
                    fileCallback = null;
                    Toast.makeText(MainActivity.this, "Couldn't open the camera or gallery", Toast.LENGTH_SHORT).show();
                    return false;
                }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String[] perms, int[] results) {
        super.onRequestPermissionsResult(requestCode, perms, results);
        boolean ok = results.length > 0 && results[0] == PackageManager.PERMISSION_GRANTED;
        if (requestCode == REQ_CAM_CAPTURE && pendingParams != null) {
            WebChromeClient.FileChooserParams p = pendingParams; pendingParams = null;
            if (ok) launchChooser(p);
            else { if (fileCallback != null) fileCallback.onReceiveValue(null); fileCallback = null;
                Toast.makeText(this, "Camera permission is needed to take photos", Toast.LENGTH_SHORT).show(); }
        } else if (requestCode == REQ_CAM_LIVE && pendingWebPerm != null) {
            PermissionRequest r = pendingWebPerm; pendingWebPerm = null;
            if (ok) r.grant(new String[]{PermissionRequest.RESOURCE_VIDEO_CAPTURE}); else r.deny();
        }
    }

    /** Links: stay inside the app for our own pages; email, phone and other sites open in their own apps. */
    private boolean handleLink(Uri uri) {
        String scheme = uri.getScheme() == null ? "" : uri.getScheme();
        String host = uri.getHost() == null ? "" : uri.getHost();
        if ((scheme.equals("https") || scheme.equals("http")) && host.equals(BuildConfig.APP_HOST)) return false;
        try {
            Intent i;
            if (scheme.equals("mailto")) i = new Intent(Intent.ACTION_SENDTO, uri);
            else i = new Intent(Intent.ACTION_VIEW, uri);
            startActivity(i);
        } catch (ActivityNotFoundException e) {
            Toast.makeText(this, "No app on this phone can open that link", Toast.LENGTH_SHORT).show();
        }
        return true;
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == REQ_UNLOCK) {
            web.evaluateJavascript("window.DRX_unlocked&&window.DRX_unlocked(" + (resultCode == RESULT_OK ? "true" : "false") + ")", null);
            return;
        }
        if (requestCode == REQ_VOICE) {
            String text = "";
            if (resultCode == RESULT_OK && data != null) {
                ArrayList<String> r = data.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);
                if (r != null && !r.isEmpty()) text = r.get(0);
            }
            String js = "window.DRX_voiceResult&&window.DRX_voiceResult(" + JSONObject.quote(voiceField == null ? "" : voiceField) + "," + JSONObject.quote(text) + ")";
            web.evaluateJavascript(js, null);
            voiceField = null;
            return;
        }
        if (requestCode != REQ_FILE || fileCallback == null) return;
        Uri[] result = null;
        if (resultCode == RESULT_OK) {
            if (cameraUri != null) {
                result = new Uri[]{cameraUri};
            } else if (data != null) {
                if (data.getClipData() != null) {
                    int n = data.getClipData().getItemCount();
                    result = new Uri[n];
                    for (int k = 0; k < n; k++) result[k] = data.getClipData().getItemAt(k).getUri();
                } else if (data.getData() != null) {
                    result = new Uri[]{data.getData()};
                }
            }
        }
        fileCallback.onReceiveValue(result);
        fileCallback = null;
        cameraUri = null;
    }

    /** Back: close an open screen inside the app first, then go back, then leave. */
    @Override
    public void onBackPressed() {
        web.evaluateJavascript("(window.DRX_back&&window.DRX_back())?'1':'0'", value -> {
            if (value != null && value.contains("1")) return;
            if (web.canGoBack()) web.goBack();
            else finishApp();
        });
    }

    private void finishApp() { super.onBackPressed(); }

    @Override
    protected void onSaveInstanceState(Bundle out) {
        super.onSaveInstanceState(out);
        web.saveState(out);
    }

    @Override
    protected void onResume() { super.onResume(); web.onResume(); }

    @Override
    protected void onPause() { web.onPause(); super.onPause(); }

    /** Called from the page to hand over a generated file (prescription PDF, backup, export). */
    private class Bridge {
        @JavascriptInterface
        public void saveFile(String base64, String filename, String mime) {
            try {
                byte[] bytes = Base64.decode(base64, Base64.DEFAULT);
                File dir = new File(getCacheDir(), "shared");
                if (!dir.exists()) dir.mkdirs();
                String safe = filename == null ? "file" : filename.replaceAll("[^A-Za-z0-9._-]", "_");
                File f = new File(dir, safe);
                try (FileOutputStream out = new FileOutputStream(f)) { out.write(bytes); }
                Uri uri = FileProvider.getUriForFile(MainActivity.this, "in.dermrx.desk.files", f);
                Intent send = new Intent(Intent.ACTION_SEND);
                send.setType(mime == null || mime.isEmpty() ? "application/octet-stream" : mime);
                send.putExtra(Intent.EXTRA_STREAM, uri);
                send.putExtra(Intent.EXTRA_SUBJECT, safe);
                send.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
                Intent chooser = Intent.createChooser(send, "Share or save " + safe);
                chooser.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
                runOnUiThread(() -> startActivity(chooser));
            } catch (Exception e) {
                runOnUiThread(() -> Toast.makeText(MainActivity.this, "Couldn't prepare the file", Toast.LENGTH_SHORT).show());
            }
        }

        @JavascriptInterface
        public String version() { return BuildConfig.VERSION_NAME; }

        /** True when the phone has a screen lock (fingerprint / face / PIN / pattern) set up. */
        @JavascriptInterface
        public boolean canUnlock() {
            KeyguardManager km = (KeyguardManager) getSystemService(KEYGUARD_SERVICE);
            return km != null && km.isDeviceSecure();
        }

        /** Ask for the phone's own fingerprint / screen lock; result returns to window.DRX_unlocked(ok). */
        @JavascriptInterface
        @SuppressWarnings("deprecation")
        public void unlock(String title) {
            runOnUiThread(() -> {
                KeyguardManager km = (KeyguardManager) getSystemService(KEYGUARD_SERVICE);
                Intent i = km == null ? null : km.createConfirmDeviceCredentialIntent(title == null || title.isEmpty() ? "Unlock Derma Desk" : title, "Use your fingerprint or screen lock");
                if (i == null) { web.evaluateJavascript("window.DRX_unlocked&&window.DRX_unlocked(false)", null); return; }
                startActivityForResult(i, REQ_UNLOCK);
            });
        }

        /** Block screenshots / screen recording while sensitive screens are open. */
        @JavascriptInterface
        public void secure(boolean on) {
            runOnUiThread(() -> {
                if (on) getWindow().addFlags(WindowManager.LayoutParams.FLAG_SECURE);
                else getWindow().clearFlags(WindowManager.LayoutParams.FLAG_SECURE);
            });
        }

        /** Voice typing through the phone's speech recogniser; result returns to window.DRX_voiceResult. */
        @JavascriptInterface
        public void listen(String fieldId, String lang) {
            runOnUiThread(() -> {
                try {
                    voiceField = fieldId;
                    Intent i = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
                    i.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
                    String l = lang == null || lang.isEmpty() ? "en-IN" : lang;
                    i.putExtra(RecognizerIntent.EXTRA_LANGUAGE, l);
                    i.putExtra(RecognizerIntent.EXTRA_LANGUAGE_PREFERENCE, l);
                    i.putExtra(RecognizerIntent.EXTRA_PROMPT, "Speak now");
                    startActivityForResult(i, REQ_VOICE);
                } catch (ActivityNotFoundException e) {
                    voiceField = null;
                    web.evaluateJavascript("window.DRX_voiceResult&&window.DRX_voiceResult('','')", null);
                    Toast.makeText(MainActivity.this, "Voice typing needs the Google app on this phone", Toast.LENGTH_LONG).show();
                }
            });
        }
    }
}
