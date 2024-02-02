from functions_all.sreality import get_re_offers

#locality_region        ={'Jihočeský kraj': 1,
                        # 'Plzeňský kraj': 2,
                        # 'Karlovarský kraj': 3,
                        # 'Ústecký kraj': 4, 
                        # 'Liberecký kraj': 5, 
                        # 'Královéhradecký kraj': 6, 
                        # 'Pardubický kraj': 7, 
                        # 'Olomoucký kraj': 8, 
                        # 'Zlínský kraj': 9, 
                        # 'Hlavní město Praha': 10,
                        # 'Středočeský kraj': 11,
                        # 'Moravskoslezský kraj': 12,
                        # 'Kraj Vysočina': 13, 
                        # 'Jihomoravský kraj': 14}

get_re_offers(path_to_sqlite="estate_data.sqlite", category_main="houses", category_type="sale", category_sub=[], locality_region=["Hlavní město Praha"])