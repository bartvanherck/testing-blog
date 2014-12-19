title: first robot framework patch
date: 2014-07-09 18:28:43
category: python
summary: Today I saw a little issue in the Robot Framework. The Robot Framework is a test automation framework for acceptance testing and acceptance test-driven development. The issue that I saw, was when running the unittests. 

Today I saw a little issue in the Robot Framework. The Robot Framework is a test automation framework for acceptance testing and acceptance test-driven development. The issue that I saw, was when running the unittests. One of them failed on my windows operating system in some cases.

The test was splitting args from letters with a colon (:) In the unittest, a test with "L:" exists, but on my windows machine that drive letter exists, so this means that the test per accident failed on my machine. So I replaced the drive letter by a number in the test and it succeeds. Here is my patch:

<code><pre>
diff --git a/utest/conf/test_settings.py b/utest/conf/test_settings.py
index c10972f..ac440ce 100644
--- a/utest/conf/test_settings.py
+++ b/utest/conf/test_settings.py
@@ -32,7 +32,7 @@ class TestSplitArgsFromNameOrPath(unittest.TestCase):
         assert not os.path.exists("foo"), "does not work if you have foo folder!" 
         assert_equals(self.method("foo:"), ("foo", [""])) 
         assert_equals(self.method("bar:arg1::arg3"), ("bar", ["arg1", "", "arg3"])) 
-        assert_equals(self.method("L:"), ("L", [""])) 
+        assert_equals(self.method("3:"), ("3", [""]))

     def test_with_windows_path_without_args(self):
         assert_equals(self.method("C:\\name.py"), ("C:\\name.py", []))
--
</pre></code>

I created on github a pull request, and I hope it get's somehow accepted. Maybe the test was correct and I need to change some **real** code, but I have to wait now what the developers deciding to do with my patch.
