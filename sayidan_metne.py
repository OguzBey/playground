
__author__ = "OguzBey"


class SayidanMetne(object):

	def __init__(self):
		self._birler =  {1:"Bir", 2:"İki", 3:"Üç", 4:"Dört", 5:"Beş", 6:"Altı",
					7:"Yedi", 8:"Sekiz", 9:"Dokuz"}
		self._onlar = {1:"On", 2:"Yirmi",3:"Otuz",4:"Kırk",5:"Elli",6:"Altmış",7:"Yetmiş",
					8:"Seksen", 9:"Doksan"}

	def _kacBasamak(self, text):
		return len(text)

	def _yuzler_oku(self, text):
		self.sayimiz = text
		yuzler = int(self.sayimiz[0])
		onlar = int(self.sayimiz[1])
		birler = int(self.sayimiz[2])
		self.okunus = ""
		if yuzler == 1:
			self.okunus = "Yüz"
		elif yuzler == 0:
			self.okunus = ""
		else:
			self.okunus = "{} Yüz".format(self._birler[yuzler])
		if onlar == 0 and birler == 0:
			return self.okunus
		elif onlar != 0 and birler == 0:
			return "{0} {1}".format(self.okunus, self._onlar[onlar])
		elif onlar == 0 and birler != 0:
			return "{0} {1}".format(self.okunus, self._birler[birler])
		self.okunus = "{0} {1} {2}".format(self.okunus, self._onlar[onlar], self._birler[birler])
		return self.okunus

	def _onlar_oku(self, text):
		self.sayimiz = text
		onlar = int(self.sayimiz[0])
		birler = int(self.sayimiz[1])
		if birler == 0:
			return "{}".format(self._onlar[onlar])
		return "{} {}".format(self._onlar[onlar], self._birler[birler])

	def _binler_oku(self, text):

		b_sayisi = len(text)
		if b_sayisi == 3:
			return "{} Bin".format(self._yuzler_oku(text))
		if b_sayisi == 2:
			return "{} Bin".format(self._onlar_oku(text))
		return "{} Bin".format(self._birler[int(text)])

	def cevir(self, sayi):
		self.sayi = str(sayi) 
		self.b_sayisi = self._kacBasamak(self.sayi) 
		print("[+] Girilen sayı {} basamaklıdır.".format(self.b_sayisi))

		if self.b_sayisi > 3:
			self.f_sayi = "{:_}".format(sayi) 
			self.l_sayi = self.f_sayi.split("_") 
		else:
			self.l_sayi = []
			self.l_sayi.append(self.sayi)

		self.kaclar = len(self.l_sayi)
		if self.kaclar == 1:
			""" birler, onlar, yüzler """
			if self.b_sayisi == 3:
				print("[>>] {}".format(self._yuzler_oku(self.sayi)))
			elif self.b_sayisi == 2:
				print("[>>] ".format(self._onlar_oku(self.sayi)))
			else:
				if sayi == 0:
					print("[>>] Sıfır")
				else:
					print("[>>] {}".format(self._birler[sayi]))
			
		elif self.kaclar == 2:
			""" binler, onbinler, yüzbinler """
			self.part_2 = self._yuzler_oku(self.l_sayi[1])
			self.part_1 = self._binler_oku(self.l_sayi[0])
			print("[>>] {} {}".format(self.part_1, self.part_2))
		else:
			pass

if __name__ == '__main__':
	girilen_sayi = int(input("Sayı giriniz: "))
	SayidanMetne().cevir(girilen_sayi)