Øving 6: Gruppeprosjekt del 1
Læringsmål
Dere skal lære å jobbe med en programmeringsoppgave i grupper. Dere skal lære enkel data-analyse
og plotting. Dere skal lære grunnleggende bruk av Git og Github.
Om CSV filer
For denne øvingen vil det bli delt ut to .csv filer. De vil ha etternavn .csv.txt slik at dere får lastet dem
ned riktig. Erfaringen min er at hos en del av dere vil ei fil med etternavn .csv bli åpnet i Excel og så
lagret som Excel-filer (etternavn .xlsx) i stedet for .csv filer lokalt på deres egne datamaskiner. Excel-
filer er binærfiler. For å lese ei Excel-fil må man bruke eksterne pakker som for eksempel Pandas, som
ikke er pensum i DAT120.
Overordnet oppgavebeskrivelse: meteorologiske data
Dere skal lese inn to separate .csv filer som inneholder sammenliknbare værdata. Den ene fila er fra
en lokal værstasjon her på UiS og kommer fra professor Rune Wiggo Time. Den andre fila er fra Sola
værstasjon og er lastet ned fra Meteorologisk institutt. Denne siste fila er under en Creative
Commons lisens som lar oss bruke dataene så lenge vi sier hvor vi fikk dataene fra. Begge filene
dekker perioden 11. til 13. juni 2021. Begge filene inneholder data om temperatur og trykk, men med
litt ulik oppløsning. Den første fila har ei linje for hver 10. sekund. Den andre fila har ei linje for hver
time.
Merk: I fila for den lokale værstasjonen så skifter formatet for datoer og tidspunkt omtrent 2/3 ut i
fila. Det er obligatorisk å håndtere formatet som er i første del av fila og så ignorere linjer med ugyldig
datoformat. Formatet i første del av fila er på formen MM.DD.ÅÅÅÅ TT:MM. Dette betyr at det er to
siffer for måned først, deretter et punktum, deretter to siffer for dag, deretter et punktum, deretter
fire siffer for år, deretter et åpenrom, deretter to siffer for timer, deretter et kolon og til slutt to siffer
for minutt. Dette er et normalt amerikansk datoformat. Sekundene ligger ikke her, men ligger i stedet
i neste kolonne, sekunder siden start. Timer er oppgitt i 24-timersformat slik at 14 betyr to om
ettermiddagen.
I fila for meteorologisk institutt er dato og tidspunkt oppgitt på formatet DD.MM.ÅÅÅÅ TT:MM
