[app]

# (str) Title of your application
title = Sensitivity Converter

# (str) Package name
package.name = sensconverter

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy==2.3.0,cython==0.29.36

# (str) Icon of the application
icon.filename = %(source.dir)s/IMG_20250817_185747.png

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = android.permission.INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK / AAB will support.
android.minapi = 24

# (bool) If True, then automatically accept SDK license agreements.
android.accept_sdk_license = True

# Python for android (p4a) specific

# (str) python-for-android branch to use
p4a.branch = develop

# (str) Bootstrap to use for android builds
p4a.bootstrap = sdl2

# (str) The format used to package the app for debug mode (apk or aar).
android.debug_artifact = apk

[buildozer]

log_level = 2
warn_on_root = 1