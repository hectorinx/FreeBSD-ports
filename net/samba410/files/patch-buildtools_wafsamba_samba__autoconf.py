--- buildtools/wafsamba/samba_autoconf.py.orig	2019-01-15 10:07:00 UTC
+++ buildtools/wafsamba/samba_autoconf.py
@@ -575,7 +575,7 @@ def library_flags(self, libs):
 
 
 @conf
-def CHECK_LIB(conf, libs, mandatory=False, empty_decl=True, set_target=True, shlib=False):
+def CHECK_LIB(conf, libs, mandatory=False, empty_decl=True, set_target=True, shlib=False, msg=None):
     '''check if a set of libraries exist as system libraries
 
     returns the sublist of libs that do exist as a syslib or []
@@ -595,11 +595,29 @@ int foo()
             ret.append(lib)
             continue
 
+        if msg is None:
+            msg = 'Checking for library %s' % lib
+
         (ccflags, ldflags, cpppath) = library_flags(conf, lib)
+
         if shlib:
-            res = conf.check(features='c cshlib', fragment=fragment, lib=lib, uselib_store=lib, cflags=ccflags, ldflags=ldflags, uselib=lib.upper(), mandatory=False)
+            res = conf.check(features='c cshlib',
+                             fragment=fragment,
+                             lib=lib,
+                             uselib_store=lib,
+                             cflags=ccflags,
+                             ldflags=ldflags,
+                             uselib=lib.upper(),
+                             mandatory=False,
+                             msg=msg)
         else:
-            res = conf.check(lib=lib, uselib_store=lib, cflags=ccflags, ldflags=ldflags, uselib=lib.upper(), mandatory=False)
+            res = conf.check(lib=lib,
+                             uselib_store=lib,
+                             cflags=ccflags,
+                             ldflags=ldflags,
+                             uselib=lib.upper(),
+                             mandatory=False,
+                             msg=msg)
 
         if not res:
             if mandatory:
@@ -927,6 +945,6 @@ def SAMBA_CHECK_UNDEFINED_SYMBOL_FLAGS(c
         conf.env.undefined_ldflags = conf.ADD_LDFLAGS('-Wl,-no-undefined', testflags=True)
 
     if not sys.platform.startswith("openbsd") and conf.env.undefined_ignore_ldflags == []:
-        if conf.CHECK_LDFLAGS(['-undefined', 'dynamic_lookup']):
+        if conf.CHECK_LDFLAGS(['-undefined', 'dynamic_lookup'] + conf.env.WERROR_CFLAGS):
             conf.env.undefined_ignore_ldflags = ['-undefined', 'dynamic_lookup']
 
