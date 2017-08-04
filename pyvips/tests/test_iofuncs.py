# vim: set fileencoding=utf-8 :

from helpers import *

class TestIofuncs(PyvipsTester):

    # test the vips7 filename splitter ... this is very fragile and annoying
    # code with lots of cases
    def test_split7(self):
        def split(path):
            filename7 = pyvips.path_filename7(path)
            mode7 = pyvips.path_mode7(path)

            return [filename7, mode7]

        cases = [
            ["c:\\silly:dir:name\\fr:ed.tif:jpeg:95,,,,c:\\icc\\srgb.icc",
                ["c:\\silly:dir:name\\fr:ed.tif", 
                 "jpeg:95,,,,c:\\icc\\srgb.icc"]],
            ["I180:",
                ["I180",
                 ""]],
            ["c:\\silly:",
                ["c:\\silly",
                 ""]],
            ["c:\\program files\\x:hello",
                ["c:\\program files\\x",
                 "hello"]],
            ["C:\\fixtures\\2569067123_aca715a2ee_o.jpg",
                ["C:\\fixtures\\2569067123_aca715a2ee_o.jpg",
                 ""]]
        ]
            
        for case in cases:
            self.assertEqualObjects(split(case[0]), case[1])

if __name__ == '__main__':
    unittest.main()
