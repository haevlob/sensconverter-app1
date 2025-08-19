[app]

title = Sensitivity Converter
package.name = sensconverter
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0  # Update to 2.3.0 if tested
orientation = portrait
fullscreen = 0
android.permissions =  # Empty is fine
android.api = 33  # Update to 33 for better compatibility
android.minapi = 21
android.accept_sdk_license = True
android.ndk = 25c  # Update to 25c
p4a.branch = develop
p4a.bootstrap = sdl2
android.debug_artifact = apk
android.skip_update = False

[buildozer]
log_level = 2
warn_on_root = 1