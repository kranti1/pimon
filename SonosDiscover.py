# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 15:16:07 2016

@author: kartiks
"""

import soco


""" Finds the Family Room Zone. """
for zone in soco.discover():
    if zone.player_name == 'Family Room':
        FamilyRoomZone = zone


# URI of library song    
FamilyRoomZone.clear_queue()
FamilyRoomZone.play_uri('x-file-cifs://Kartiks-iMac/Music/Vinoo%20music/Carnatic/Carnatic%20Instrumental/U.%20Srinivas/Mandolin%20Ecstasy/01%20Sarasijaksha-Kambodhi-Ata.mp3')
FamilyRoomZone.add_uri_to_queue('x-file-cifs://Kartiks-iMac/Music/Vinoo%20music/Carnatic/Jan%2006/MS%20Subbulakshmi/Slokas/Suprabatham.mp3')

# Uri for 710 Kiro
#zone.play_uri('x-rincon-mp3radio://13743.live.streamtheworld.com:80/KIROAM_SC?TGT=TuneIn&DIST=TuneIn')
 
 