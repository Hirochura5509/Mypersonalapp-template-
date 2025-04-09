[app]
title = MyPersonalApp
package.name = mypersonalapp
package.domain = org.mypersonalapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
icon.filename = assets/icon.png
fullscreen = 1
orientation = portrait

[buildozer]
log_level = 2

[android]
android.api = 34
android.ndk = 23b
android.sdk = 34
requirements = python3,kivy