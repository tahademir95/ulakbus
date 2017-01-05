# -*-  coding: utf-8 -*-

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.

"""HITAP Askerlik Guncelle

Hitap'a personelin askerlik bilgilerinin eklenmesini yapar.

"""

from ulakbus.services.personel.hitap.hitap_guncelle import HITAPGuncelle


class HizmetAskerlikGuncelle(HITAPGuncelle):
    """
    HITAP Guncelleme servisinden kalıtılmış Hizmet Askerlik Bilgisi Guncelleme servisi

    """
    HAS_CHANNEL = True
    service_dict = {
        'service_name': 'HizmetAskerlikUpdate',
        'fields': {
            'kayitNo': 'kayit_no',
            'askerlikNevi': 'askerlik_nevi',
            'baslamaTarihi': 'baslama_tarihi',
            'bitisTarihi': 'bitis_tarihi',
            'kitaBaslamaTarihi': 'kita_baslama_tarihi',
            'kitaBitisTarihi': 'kita_bitis_tarihi',
            'muafiyetNeden': 'muafiyet_neden',
            'sayilmayanGunSayisi': 'sayilmayan_gun_sayisi',
            'sinifOkuluSicil': 'sinif_okulu_sicil',
            'subayliktanErligeGecisTarihi':
                'subayliktan_erlige_gecis_tarihi',
            'subayOkuluGirisTarihi': 'subay_okulu_giris_tarihi',
            'tckn': 'tckn',
            'tegmenNaspTarihi': 'tegmen_nasp_tarihi',
            'gorevYeri': 'gorev_yeri',
            'kurumOnayTarihi': 'kurum_onay_tarihi',
            'astegmenNaspTarihi': 'astegmen_nasp_tarihi',
        },
        'date_filter': ['baslamaTarihi', 'bitisTarihi', 'kitaBaslamaTarihi', 'kitaBitisTarihi',
                        'subayliktanErligeGecisTarihi', 'subayOkuluGirisTarihi',
                        'tegmenNaspTarihi', 'kurumOnayTarihi', 'astegmenNaspTarihi'],
        'required_fields': ['kayitNo', 'tckn', 'askerlikNevi', 'kurumOnayTarihi']
    }
