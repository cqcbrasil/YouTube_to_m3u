#! /usr/bin/python3

banner1 = r'''
###########################################################################
#                                                                         #
#                                  >> https://github.com/cqcbrasil        #
###########################################################################
#EXTM3U


#EXTINF:0 tvg-id="ext" group-title="Locales",Camaras de Villa Gesell (Av. 3 y 104)
http://cam104y3.gesell.com.ar/playlist.m3u8
#EXTINF:0 tvg-id="ext" group-title="Locales",Camaras de Villa Gesell (Buenos Aires y Playa)
http://cambsasyplaya.gesell.com.ar/playlist.m3u8
#EXTINF:0 tvg-id="ext" group-title="Locales",Camaras de Villa Gesell (La Pinocha)
http://camlapinocha.gesell.com.ar/playlist.m3u8

#EXTINF:-1 tvg-id="America TV Argentina" tvg-name="America TV Argentina" tvg-logo="https://imagenes.gatotv.com/logos/canales/oscuros/america_tv_argentina.png" group-title="Argentina",America TV | Argentina - TDA 2.1
https://dai.google.com/linear/hls/pa/event/OY2i_lL4SMyXE5Zaj4ULEg/stream/a1d5eebc-fe78-4cbb-ac5c-08cf52e94064:SCL/master.m3u8

#EXTINF:-1 tvg-logo="https://scontent.fepa11-1.fna.fbcdn.net/v/t1.6435-9/206638151_10223169123710059_3666810289391430657_n.jpg?_nc_cat=101&ccb=1-3&_nc_sid=825194&_nc_eui2=AeGxugJ54qa7RhgKBnLTrHOu14OonvQq8lrXg6ie9CryWkCQzaYyrufVmZGkiprZVM0&_nc_ohc=dbLCQPiMFxEAX9X0jrT&_nc_ht=scontent.fepa11-1.fna&oh=afeef92e5377cb7720df7b2f4afc60c8&oe=6127F95F" group-title="Argentina",SSIPTV ARG TV - TDA 6.2
http://service-stitcher.clusters.pluto.tv/stitch/hls/channel/5df265697ec3510009df1ef0/master.m3u8?advertisingId=&appName=web&appVersion=unknown&appStoreUrl=&architecture=&buildVersion=&clientTime=0&deviceDNT=0&deviceId=bff1d530-6307-11eb-b3fa-019cb96f121b&deviceMake=Chrome&deviceModel=web&deviceType=web&deviceVersion=unknown&includeExtendedEvents=false&sid=ec2383fd-6e28-4df5-9d1c-b66eee7000c&userId=&serverSideAds=true

#EXTINF:-1 tvg-id="Television Publica" tvg-name="Television Publica" tvg-logo="https://i.imgur.com/04nIdpc.png" group-title="Argentina",Television Publica | Argentina - TDA 7.1
https://cntlnk-main-edge-access.secure.footprint.net/entrypoint/c7_vivo01_dai_source-20001_all_1080p.m3u8



#EXTINF:-1 tvg-id="Television Publica" tvg-name="Television Publica" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/0/0a/Logo_Televisi%C3%B3n_P%C3%BAblica_Argentina.png" group-title="Argentina",TV PUBLICA - SINAL ORIGINAL 2 - TDA 7.1
https://s@cntlnk-main-edge-access.secure.footprint.net/entrypoint/c7_vivo01_dai_source-20001_all_1080p.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Telefe_%28nuevo_logo%29.png/800px-Telefe_%28nuevo_logo%29.png" group-title="Argentina",TELECOLORMUX - TDA 8.1
https://live.obslivestream.com/telecolormux/tracks-v1a1/mono.m3u8



#EXTINF:-1 tvg-id="Telefe" tvg-name="Telefe" tvg-logo="https://imagenes.gatotv.com/logos/canales/oscuros/telefe_argentina.png" group-title="Argentina",Telefe | Argentina - TDA 11.1
https://cdn2.eco.cdn.moderntv.eu/econocable/stream/TELEFE/40-hls/live-media.m3u8?_cdn_attrs=account%3Deconocable%2Cresource%3DTELEFE_stream_te&_cdn_session=932321571&_cdn_timestamp=1688435981&_cdn_token=eb657393320d61ba109ce5db6d52a3ce8017e904

#EXTINF:-1 tvg-id="Telefe" tvg-name="Telefe" tvg-logo="https://imagenes.gatotv.com/logos/canales/oscuros/telefe_argentina.png" group-title="Argentina",Telefe | Argentina - TDA 11.1
https://v3.playerlatino.live/stream/m3u8/771



#EXTINF:-1 tvg-id="Telefe" tvg-name="Telefe" tvg-logo="https://telefe-static.akamaized.net/media/18154476/logo-telefe-twitter.png" group-title="Argentina", Telefe (VPN) - TDA 11.1
https://mitelefe.com/Api/Videos/GetSourceUrl/694564/0/HLS

#EXTINF:-1 tvg-id="Telefe" tvg-name="Telefe" tvg-country="AR" tvg-logo="http://x.playerlatino.live/telefe.png" group-title="Argentina", Telefe (VPN) 2 - TDA 11.1
https://telefe.com/Api/Videos/GetSourceUrl/694564/0/HLS?.m3u8

#EXTINF:-1 tvg-id="13 de Argentina" tvg-name="13 de Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/45/Eltrece_logotipo_2018.png" group-title="Argentina", El Trece - TDA 13.1
https://livetrx01.vodgc.net/eltrecetv/index.m3u8

#EXTINF:-1 tvg-id="13 de Argentina" tvg-name="13 de Argentina" tvg-logo="http://schedulesdirect-api20141201-logos.s3.dualstack.us-east-1.amazonaws.com/stationLogos/s16044_dark_360w_270h.png" group-title="Argentina", El Trece 2 - TDA 13.1
https://v3.playerlatino.live/stream/m3u8/767

#EXTINF:-1 tvg-id="El Nueve AR" tvg-name="El Nueve AR" tvg-country="AR" tvg-logo="https://vignette.wikia.nocookie.net/logopedia/images/f/f7/Canal-nueve-ar2017.png" group-title="Argentina", CANAL 9 35.1 - TDA 35.1
https://2a1773fcc0c94a639b422d1cf7ba14b7.mediatailor.us-east-1.amazonaws.com/v1/master/4c8323052bc3dbd9aa2eba0b638d8495561e8377/JW-Octubre-Channel09/live/channel09/live.isml/.m3u8
#EXTM3U https://00475e6934d74fe48a80427567a45918.mediatailor.us-east-1.amazonaws.com/v1/manifest/4c8323052bc3dbd9aa2eba0b638d8495561e8377/JW-Octubre-Channel09/0df6d88d-304a-4d15-9cf8-eab1bc9b5e45/3.m3u8
#EXTM3U https://00475e6934d74fe48a80427567a45918.mediatailor.us-east-1.amazonaws.com/v1/master/4c8323052bc3dbd9aa2eba0b638d8495561e8377/JW-Octubre-Channel09/live/channel09/live.isml/b00d164f-be51-473e-a47c-b33aa1f44186.m3u8




#EXTINF:-1 tvg-logo="https://image.winudf.com/v2/image1/Y29tLmExMjNmcmVlYXBwcy5mcmVlLmFwcDVkNWVjMWY4ODliOThfaWNvbl8xNTY3NjE5OTcxXzAxNw/icon.png?w=170&fakeurl=1" group-title="Argentina",CANAL 4 TELEAIRE SAN MARTIN - TDA 21.1
https://stmvideo2.livecastv.com/canal4/canal4/playlist.m3u8

#EXTINF:-1 tvg-name="Cronica TV" tvg-name="Cronica TV" tvg-logo="http://schedulesdirect-api20141201-logos.s3.dualstack.us-east-1.amazonaws.com/stationLogos/s16258_dark_360w_270h.png" group-title="Argentina",Cronica TV | Argentina - TDA 22.1
http://tv.dominiotv.xyz:25461/live/Rolando/Rolando2021/52503.ts



#EXTINF:-1 tvg-id="America TV Argentina" tvg-name="America TV Argentina" tvg-logo="https://imagenes.gatotv.com/logos/canales/oscuros/america_tv_argentina.png" group-title="Argentina",MILENIO TV
http://tv.dominiotv.xyz:25461/live/Rolando/Rolando2021/52487.ts

#EXTINF:-1 tvg-id="IP" tvg-name="Informacion Periodistica" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Informaci%C3%B3n_Period%C3%ADstica_IP_Logo.svg/260px-Informaci%C3%B3n_Period%C3%ADstica_IP_Logo.svg.png" group-title="Argentina",Informacion Periodistica | Argentina - TDA 24.5
https://d1nmqgphjn0y4.cloudfront.net/live/ip/live.isml/live-audio_1=128000-video=4499968.m3u8

#EXTINF:-1 tvg-id="IP" tvg-name="Informacion Periodística" tvg-logo="https://i.imgur.com/SQSu9M5.png" group-title="Argentina",Informacion Periodística | Argentina - TDA 24.5
https://octubre-live.cdn.vustreams.com/live/ip/live.isml/live-audio_1=128000-video=2800000.m3u8

#EXTINF:-1 tvg-id="IP" tvg-name="IP" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdQ4CbRDh4Wgxt0o_pw9V-kw9Vz6T0Re2Q_RD62jp7cZMO0uWvSKSUN6sZ2vjYcbn5fAs&usqp=CAU" group-title="Argentina",IP | Argentina - TDA 24.5
https://d1nmqgphjn0y4.cloudfront.net/live/ip/live.isml/live-audio_1=128000-video=729984.m3u8

#EXTINF:-1 tvg-logo="http://tvabierta.weebly.com/uploads/5/1/3/4/51344345/unife.png" group-title="Argentina",UNIFE 25.1 - TDA 25.1
https://dacastmmd.mmdlive.lldns.net/dacastmmd/fafa592f5b7b4212928307608b85bdf7/chunklist_b4628000.m3u8

#EXTINF:-1 tvg-id="C5N" tvg-name="C5N" tvg-logo="https://cdn.mitvstatic.com/channels/ar_c5n_m.png" group-title="Argentina",C5N | Argentina - TDA 26.1
https://ythls.onrender.com/channel/UCFgk2Q2mVO1BklRQhSv6p0w.m3u8

#EXTINF:-1 tvg-id="A24" tvg-name="America 24" tvg-logo="https://cdn.mitvstatic.com/channels/ar_america-24_m.png" group-title="Argentina",America 24 | Argentina - TDA 27.1
https://ythls.onrender.com/channel/UCR9120YBAqMfntqgRTKmkjQ.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Net_TV_logo.png/120px-Net_TV_logo.png" group-title="Argentina",NET TV 27.2 - TDA 27.2
https://unlimited1-us.dps.live/nettv/nettv.smil/nettv/livestream1/playlist.m3u8






#EXTINF:-1 tvg-logo="https://cmmusica.com.ar/images/logo.png" group-title="Argentina",CM TV | Argentina - TDA 33.1
https://g5.proy-hor.transport.edge-access.net/a09/ngrp:CM_CanaldelaMusica-100044_all/CM_CanaldelaMusica-100044_540p.m3u8










#EXTINF:-1 tvg-id="Glitz" tvg-name="Glitz" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/b/b7/Glitzlogo.png" group-title="Argentina",Glitz | Argentina
http://tv.dominiotv.xyz:25461/live/Rolando/Rolando2021/52509.ts


'''


banner2 = r'''
#EXTM3U


#EXTINF:-1 tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal Nueve Multivisi n (AR) - TDA 20.1
http://panel.dattalive.com:1935/8250/8250/playlist.m3u8

#EXTINF:-1 tvg-id="Canal 4 San Juan" tvg-name="Canal 4 San Juan" tvg-logo="http://www.canal4sanjuan.com.ar/digital/images/logo-cir.png" group-title="Argentina",Canal 4 San Juan | Argentina - TDA 22.1
http://streamlov.alsolnet.com/canal4sanjuan/live/chunklist_w1603184235.m3u8

#EXTINF:-1 tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal 26 (San Justo-Arg.) - TDA 22.2
http://live-edge01.telecentro.net.ar/live/smil:c26.smil/chunklist_w858131162_b414000_sleng.m3u8

#EXTINF:-1 tvg-id="Tec TV" tvg-name="Tec TV" tvg-logo="https://www.tec.gob.ar/wp-content/uploads/2022/05/Tec-logo.png" group-title="Argentina",Tec TV | Argentina - TDA 22.4
https://tv.initium.net.ar:3939/live/tectvmainlive.m3u8

#EXTINF:-1 tvg-id="DeporTV Argentina" tvg-name="DeporTV Argentina" tvg-logo="https://i2.paste.pics/7b99edf751cc110abb5fd3f040e558b8.png" group-title="Argentina",DeporTV | Argentina - TDA 24.1
https://5fb24b460df87.streamlock.net/live-cont.ar/deportv/playlist.m3u8


#EXTINF:-1 tvg-id="N/A" group-title="Argentina" tvg-logo="https://www.cxtv.com.br/img/Tvs/Logo/webp-l/d800ee1a28bbee6769de24c5c050c40c.webp",Canal Once - TDA 24.3
https://vivo.canaloncelive.tv/alivepkgr3/ngrp:cepro_all/playlist.m3u8


#EXTINF:-1 tvg-id="NET TV" tvg-name="NET TV" tvg-logo="https://www.canalnet.tv/_templates/desktop/includes/img/logo.png" group-title="Argentina",NET TV | Argentina - TDA 27.2
https://unlimited1-us.dps.live/nettv/nettv.smil/nettv/livestream2/chunks.m3u8

#EXTINF:-1 tvg-id="Canal 4 Jujuy" tvg-name="Canal 4 Jujuy" tvg-logo="https://s3.amazonaws.com/static-c4-1/assets/img/logos/elcuatro-logo-100x124.png" group-title="Argentina",Canal 4 Jujuy | Argentina - TDA 26.1
https://5cd577a3dd8ec.streamlock.net/canal4/manifest.smil/chunklist_w92188071_b316000.m3u8

#EXTINF:-1 tvg-id="Canal 4 Jujuy" tvg-name="Canal 4 Jujuy" tvg-logo="https://s3.amazonaws.com/static-c4-1/assets/img/logos/elcuatro-logo-100x124.png" group-title="Argentina",Canal 4 Jujuy | Argentina - TDA 26.2
https://5cd577a3dd8ec.streamlock.net/canal4/smil:manifest.smil/chunklist_w1908572533_b316000.m3u8

#EXTINF:-1 tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal 3ABN latino - TDA 32.1
http://uni5rtmp.tulix.tv:1935/bettervida/bettervida/playlist.m3u8


#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal 5atv
http://www.coninfo.net:1935/tvcinco/live1/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal Nueve Multivisi n (AR)
http://api.new.livestream.com/accounts/679322/events/3782013/live.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal Nueve Multivisi n (AR)
http://panel.dattalive.com:1935/8204/8204/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal Nueve Multivisi n (AR)
http://stmv4.questreaming.com/fenixlarioja/fenixlarioja/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal Nueve Multivisi n (AR)
https://5f700d5b2c46f.streamlock.net/madryntv/madryntv/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal Nueve Multivisi n (AR)
http://arcast.net:1935/mp/mp/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal Nueve Multivisi n (AR)
https://panel.dattalive.com/8250/8250/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal Nueve Multivisi n (AR)
http://coninfo.net:1935/chacodxdtv/live/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal Nueve Multivisi n (AR)
http://panel.dattalive.com:1935/8250/8250/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal Nueve Multivisi n (AR)
https://unlimited1-us.dps.live/nettv/nettv.smil/nettv/livestream1/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal Nueve Multivisi n (AR)
https://panel.seo.tv.bo:3337/live/franzbalboa2live.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal Nueve Multivisi n (AR)
https://tastemade-es8intl-roku.amagi.tv/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal Nueve Multivisi n (AR)
http://www.coninfo.net:1935/previsoratv/live/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal Nueve Multivisi n (AR)
http://live-edge01.telecentro.net.ar/live/smil:trm.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal Nueve Multivisi n (AR)
http://cdnh4.iblups.com/hls/irtp.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal Nueve Multivisi n (AR)
https://59a564764e2b6.streamlock.net/vallenato/Vallenato2/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal Nueve Multivisi n (AR)
https://5f700d5b2c46f.streamlock.net/vertv/vertv/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Telemax  HD Argent.
http://live-edge01.telecentro.net.ar/live/smil:tlx.smil/chunklist_w950122583_b1828000_sleng.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",24/7 Canal de Noticias
http://59c5c86e10038.streamlock.net:1935/6605140/6605140/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",5RTV Santa Fe
http://api.new.livestream.com/accounts/22636012/events/8242619/live.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",5TV (Corrientes) (480p)
http://www.coninfo.net:1935/tvcinco/live1/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",5TV Corrientes
http://www.coninfo.net:1935/tvcinco/live1/chunklist_w1546509083.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Ciudad TV Chaco
http://coninfo.net:1935/chacodxdtv/live/chunklist_w1251301598.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Music TOP
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/chunklist_w1582140541_b364000_sleng.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Music Top
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/chunklist_w538311571_b364000_sleng.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="277" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/277_Canal_XFN.png",Canal XFN * | AR
https://streamconex.com:1936/canalxfn/canalxfn/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="1026" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/1026_Tele_Mix.png",Tele Mix * | AR
https://panel.dattalive.com:443/8068/8068/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="251" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/251_13_Max_Television.png",13 Max Television | AR
http://coninfo.net:1935/13maxhd/live13maxtvnuevo_720p/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="249" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/249_5TV.png",5TV | AR
http://www.coninfo.net:1935/tvcinco/live1/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="215" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/215_Azahares_Radio_Multimedia.png",Azahares Radio Multimedia | AR
http://streamyes.alsolnet.com/azaharesfm/live/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="224" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/224_Cadena_103.png",Cadena 103 | AR
http://arcast.net:1935/cadena103/cadena103/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="299" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/299_Canal_10_Rio_Negro.png",Canal 10 Rio Negro | AR
https://panel.dattalive.com:443/8204/8204/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="268" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/268_Canal_12_Madryn_TV.png",Canal 12 Madryn TV | AR
https://5f700d5b2c46f.streamlock.net:443/madryntv/madryntv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="227" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/227_Canal_13_La_Rioja.jpg",Canal 13 La Rioja | AR
http://arcast.net:1935/mp/mp/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="228" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/228_Canal_2_Jujuy.png",Canal 2 Jujuy | AR
http://api.new.livestream.com/accounts/679322/events/3782013/live.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="230" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/230_Canal_22_Buenos_Aires.jpg",Canal 22 Buenos Aires | AR
https://5f700d5b2c46f.streamlock.net:443/canal22/canal22/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="259" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/259_Canal_4_Posadas.png",Canal 4 Posadas | AR
http://iptv.ixfo.com.ar:8081/live/C4POS/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="236" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/236_Canal_9_Litoral.png",Canal 9 Litoral | AR
https://stream.arcast.live/ahora/ahora/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="273" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/273_Canal_907_FM_Comunicar.png",Canal 907 FM Comunicar | AR
https://panel.dattalive.com/canal907/canal907/chunklist_w1205944599.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="275" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/275_Canal_Coop.png",Canal Coop | AR
https://panel.dattalive.com:443/8138/8138/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="237" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/237_Ciudad_TV.jpg",Ciudad TV | AR
http://coninfo.net:1935/chacodxdtv/live/chunklist_w1251301598.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="239" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/239_Fenix.jpg",Fenix | AR
https://stmvideo1.livecastv.com/fenixlarioja/fenixlarioja/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="212" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/212_Link_TV.png",Link TV | AR
https://panel.dattalive.com:443/8128_1/8128_1/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="795" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/795_Metropolitana_FM.png",Metropolitana FM | AR
https://panel.dattalive.com/MetropolitanaFM/MetropolitanaFM/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="284" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/284_Multivision.png",Multivisi n | AR
https://panel.dattalive.com:443/8250/8250/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="243" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/243_Power.png",Power | AR
https://live2.tensila.com/1-1-1.power-tv/hls/master.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="210" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/210_Radiocanal_San_Francisco.png",Radiocanal San Francisco | AR
http://204.199.3.2/.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="308" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/308_Tele_Estrella.png",Tele Estrella | AR
https://stmvideo2.livecastv.com/telestrella/telestrella/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="290" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/290_Telecreativa.png",Telecreativa | AR
https://panel.dattalive.com:443/8012/8012/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="245" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/245_Telediez.jpg",Telediez | AR
https://videohd.live:19360/8020/8020.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="814" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/814_TeleNord.jpg",TeleNord | AR
http://www.coninfo.net:1935/previsoratv/live/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="248" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/248_Uni_Teve.png",Uni Teve | AR
https://vivo.solumedia.com:19360/uniteve/uniteve.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="207" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/207_Orbe_21.jpg",Orbe 21 | AR
https://cdn2.zencast.tv:30443/orbe/orbe21smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="1003" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/1003_Sublime_Gracia_TV.png",Sublime Gracia TV | AR
https://5f700d5b2c46f.streamlock.net:443/sublime/sublime/playlist.m3u8?PlaylistM3UCL

'''

import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://archive.org/download/lbry-8770e4ee5844471adfdbe455230483e39ea1d0e1/8770e4ee5844471adfdbe455230483e39ea1d0e1.mp4')
                return
            os.system(f'wget {url} -O temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://archive.org/download/lbry-8770e4ee5844471adfdbe455230483e39ea1d0e1/8770e4ee5844471adfdbe455230483e39ea1d0e1.mp4')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print('﻿#EXTM3U x-tvg-url="https://github.com/luisms123/tdt/raw/master/guiaxmltv.xml.gz"')


print(banner1)

#s = requests.Session()
with open('../ARGENTINA.txt', errors="ignore") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
print(banner2)
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
    
    
