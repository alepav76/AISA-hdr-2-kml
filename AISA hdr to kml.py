# Nome file: DJIL2_Camera_Positions.py
# Copyright (C) 2025 Alessandro Pavan
#
# Questo programma è software libero: puoi ridistribuirlo e/o
# modificarlo secondo i termini della GNU General Public License
# come pubblicata dalla Free Software Foundation, versione 3.
#
# Questo programma è distribuito nella speranza che sia utile,
# ma SENZA ALCUNA GARANZIA; senza neppure la garanzia implicita
# di COMMERCIABILITÀ o di IDONEITÀ PER UN PARTICOLARE SCOPO.
# Vedi la GNU General Public License per ulteriori dettagli.
#
# Dovresti aver ricevuto una copia della GNU General Public License
# insieme a questo programma. In caso contrario, vedi <https://www.gnu.org/licenses/>.

import glob

filelist = []
startlats = []
startlongs = []
endlats = []
endlongs = []
strips = []

for filename in glob.glob('*.hdr'):
    filelist.append(filename)
    
for filename in filelist:
    hdr=open(filename).readlines()
    startlats.append(hdr[8].split()[4][1:-1])
    startlongs.append(hdr[8].split()[5][0:-1])
    endlats.append(hdr[9].split()[4][1:-1])
    endlongs.append(hdr[9].split()[5][0:-1])
    strips.append(filename[5:9])
    
with open (filename[:4]+'_hdr.kml','w') as f:
    s1 = '<?xml version="1.0" encoding="UTF-8"?> \n'
    s1 += '<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom"> \n'
    s1 += '<Document> \n'
    s1 += '<name>strip log</name> \n'
    
    # definisco lo stile per i punti di partenza
    s1 += '<Style id="inizio"> \n' 
    s1 += '<IconStyle><color> ffff9900 </color> \n'
    s1 += '<Icon>http://maps.google.com/mapfiles/kml/shapes/shaded_dot.png</Icon></IconStyle> \n'
    s1 += '</Style> \n'                                                                                                                                                                                                                                                                                                     
     
    s1 += '<Style id="sn_ylw-pushpin"> \n'
    s1 += '		<IconStyle> \n'
    s1 += '			<scale>1.1</scale> \n'
    s1 += '		<Icon> \n'
    s1 += '			<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href> \n'
    s1 += '		</Icon> \n'
    s1 += '		<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/> \n'
    s1 += '	</IconStyle> \n'
    s1 += '    <LineStyle> \n'
    s1 += '		<color>ffffaa00</color> \n'
    s1 += ' <width>2</width> \n'
    s1 += '</LineStyle> \n'
    s1 += '</Style> \n'
    s1 += '<StyleMap id="msn_ylw-pushpin"> \n'
    s1 += '	<Pair> \n'
    s1 += '		<key>normal</key> \n'
    s1 += '		<styleUrl>#sn_ylw-pushpin</styleUrl> \n'
    s1 += '	</Pair> \n'
    s1 += '	<Pair> \n'
    s1 += '		<key>highlight</key> \n'
    s1 += '		<styleUrl>#sh_ylw-pushpin</styleUrl> \n'
    s1 += '	</Pair> \n'
    s1 += '</StyleMap> \n'
    s1 += '<Style id="sh_ylw-pushpin"> \n'
    s1 += '	<IconStyle> \n'
    s1 += '		<scale>1.3</scale> \n'
    s1 += '		<Icon> \n'
    s1 += '			<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href> \n'
    s1 += '		</Icon> \n'
    s1 += '		<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/> \n'
    s1 += '	</IconStyle> \n'
    s1 += '	<LineStyle> \n'
    s1 += '		<color>ffffaa00</color> \n'
    s1 += '		<width>2</width> \n'
    s1 += '	</LineStyle> \n'
    s1 += '</Style> \n'
    f.write(s1)    
      
    # disegno le linee e i punti di partenza
    for i in range(len(strips)): 
        
        # linee
        s2 = '<Placemark> \n'
        s2 += '<name> %s </name> \n'  % (strips[i])
        s2 += '<description> %s </description> \n' % (strips[i])
        s2 += '<styleUrl>#msn_ylw-pushpin</styleUrl> \n'
        s2 += '<LineString> \n'
        s2 += '	<tessellate>1</tessellate> \n'
        s2 += '	<coordinates> %s,%s,0 %s,%s,0 </coordinates> \n' % (startlongs[i], startlats[i], endlongs[i], endlats[i])
        s2 += '</LineString>  \n </Placemark>'
        f.write(s2)
        
        # punti di partenza
        s3 = '<Placemark> \n'
        #s3 += '<name> %s </name> \n'  % (co2s[i])      
        s3 += '<description>%s START</description> \n' % (strips[i]) 
        s3 += '<styleUrl>#inizio'
   
        s3 += '</styleUrl> \n'
        s3 += '<Point> \n'
        s3 += '<coordinates> %s, %s  </coordinates> \n' % (startlongs[i], startlats[i])
        s3 += '</Point> \n'
        s3 += '</Placemark> \n'
        f.write (s3)
        
        
    s4 = '</Document> \n </kml>'
    f.write(s4)
  
        
        
        
