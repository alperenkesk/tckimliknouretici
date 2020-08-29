import random

while True:

	a=random.randint(1,9)
	b=random.randint(0,9)
	c=random.randint(0,9)
	d=random.randint(0,9)
	e=random.randint(0,9)
	f=random.randint(0,9)
	g=random.randint(0,9)
	h=random.randint(0,9)
	k=random.randint(0,9)
	l=random.randint(0,9)

	m=random.randint(0,9)
	toplam=a+b+c+d+e+f+g+h+k+l
	inttostr = str(toplam)
	sonhane=inttostr[1:2]
	strtoint=int(sonhane)

	if strtoint == m:
		yenia=str(a)
		yenib=str(b)
		yenic=str(c)
		yenid=str(d)
		yenie=str(e)
		yenif=str(f)
		yenig=str(g)
		yenih=str(h)
		yenik=str(k)
		yenil=str(l)
		yenim=str(m)
		print('TC Kimlik NO:',yenia+yenib+yenic+yenid+yenie+yenif+yenig+yenih+yenik+yenil+yenim)
		break
