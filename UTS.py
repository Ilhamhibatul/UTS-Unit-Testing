# Import library unittest untuk membuat unit test
import unittest

# Fungsi pertama: menambahkan dua bilangan
def tambah(a, b):
    return a + b

# Fungsi kedua: mengurangkan dua bilangan
def kurang(a, b):
    return a - b

# Fungsi ketiga: mengalikan dua bilangan
def kali(a, b):
    return a * b

# Fungsi keempat: membagi dua bilangan
def bagi(a, b):
    return a / b

# Fungsi kelima: menghitung luas segitiga
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

# Unit test untuk fungsi tambah
class TestTambah(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(tambah(3, 5), 8)
        self.assertEqual(tambah(0, 0), 0)
        self.assertEqual(tambah(-3, 3), 0)

# Unit test untuk fungsi kurang
class TestKurang(unittest.TestCase):
    def test_kurang(self):
        self.assertEqual(kurang(5, 3), 2)
        self.assertEqual(kurang(0, 0), 0)
        self.assertEqual(kurang(-3, 3), -6)

# Unit test untuk fungsi kali
class TestKali(unittest.TestCase):
    def test_kali(self):
        self.assertEqual(kali(2, 3), 6)
        self.assertEqual(kali(0, 0), 0)
        self.assertEqual(kali(-3, 3), -9)

# Unit test untuk fungsi bagi
class TestBagi(unittest.TestCase):
    def test_bagi(self):
        self.assertEqual(bagi(6, 3), 2)
        self.assertEqual(bagi(0, 5), 0)
        self.assertEqual(bagi(-9, 3), -3)

# Unit test untuk fungsi luas_segitiga
class TestLuasSegitiga(unittest.TestCase):
    def test_luas_segitiga(self):
        self.assertEqual(luas_segitiga(4, 5), 10)
        self.assertEqual(luas_segitiga(0, 0), 0)
        self.assertEqual(luas_segitiga(3, 2), 3)

# Menjalankan unit test
if __name__ == '__main__':
    unittest.main()
