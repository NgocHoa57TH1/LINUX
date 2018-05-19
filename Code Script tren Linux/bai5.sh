echo " chuong trinh tinh tong 1 -$1"
vt=0
tong=0
while [$vt-lt$1]
do
	vt = $(($vt+1))
	tong = $(($tong+$vt))
done
echo " tong 1 - $1 = $tong"
exit 0

