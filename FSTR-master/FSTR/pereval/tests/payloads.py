valid_pereval_test_data = {
            'beauty_title': 'пер. ',
            'title': 'Пхия',
            'other_titles': 'Триев',
            'connect': '',
            'user': {
                'email': 'qwerty@mail.ru',
                'fam': 'Пупкин',
                'name': 'Василий',
                'otc': 'Иванович',
                'phone': '+7 555 55 55'
              },
            'coords': {
                'height': 1200,
                'latitude': 45.3842,
                'longtitude': 7.1525
              },
            'level': {
                'winter': '',
                'summer': '1А',
                'autumn': '1А',
                'spring': ''
              },
            'images': [
                {
                  'title': 'Седловина',
                  'data': 'https://images.com/image1.jpg'
                },
                {
                    'title': 'Подъём',
                    'data': 'https://images.com/image2.jpg'
                }
              ]
            }

missing_user_test_data = {
            'beauty_title': 'пер. ',
            'title': 'Пхия',
            'other_titles': 'Триев',
            'connect': '',
            'coords': {
                'height': 1200,
                'latitude': 45.3842,
                'longtitude': 7.1525
              },
            'level': {
                'winter': '',
                'summer': '1А',
                'autumn': '1А',
                'spring': ''
              },
            'images': [
                {
                  'title': 'Седловина',
                  'data': 'https://images.com/image1.jpg'
                },
                {
                    'title': 'Подъём',
                    'data': 'https://images.com/image2.jpg'
                }
              ]
            }

missing_coords_test_data = {
            'beauty_title': 'пер. ',
            'title': 'Пхия',
            'other_titles': 'Триев',
            'connect': '',
            'user': {
                'email': 'qwerty@mail.ru',
                'fam': 'Пупкин',
                'name': 'Василий',
                'otc': 'Иванович',
                'phone': '+7 555 55 55'
              },
            'level': {
                'winter': '',
                'summer': '1А',
                'autumn': '1А',
                'spring': ''
              },
            'images': [
                {
                  'title': 'Седловина',
                  'data': 'https://images.com/image1.jpg'
                },
                {
                    'title': 'Подъём',
                    'data': 'https://images.com/image2.jpg'
                }
              ]
            }

missing_level_test_data = {
            'beauty_title': 'пер. ',
            'title': 'Пхия',
            'other_titles': 'Триев',
            'connect': '',
            'user': {
                'email': 'qwerty@mail.ru',
                'fam': 'Пупкин',
                'name': 'Василий',
                'otc': 'Иванович',
                'phone': '+7 555 55 55'
              },
            'coords': {
                'height': 1200,
                'latitude': 45.3842,
                'longtitude': 7.1525
              },
            'images': [
                {
                  'title': 'Седловина',
                  'data': 'https://images.com/image1.jpg'
                },
                {
                    'title': 'Подъём',
                    'data': 'https://images.com/image2.jpg'
                }
              ]
            }

missing_images_test_data = {
            'beauty_title': 'пер. ',
            'title': 'Пхия',
            'other_titles': 'Триев',
            'connect': '',
            'user': {
                'email': 'qwerty@mail.ru',
                'fam': 'Пупкин',
                'name': 'Василий',
                'otc': 'Иванович',
                'phone': '+7 555 55 55'
              },
            'coords': {
                'height': 1200,
                'latitude': 45.3842,
                'longtitude': 7.1525
              },
            'level': {
                'winter': '',
                'summer': '1А',
                'autumn': '1А',
                'spring': ''
              }
            }

patch_valid_payload = {
            "title": "Changed Title",
            "user": {
                "email": "user1@mail.ru",
                "fam": "Фамилия 1",
                "name": "Имя 1",
                "otc": "Отчество 1",
                "phone": "+11111111111"
            }
        }

patch_changed_user_payload = {
            "title": "Changed Title",
            "user": {
                "email": "user1@mail.ru",
                "fam": "Фамилия 0",
                "name": "Имя 1",
                "otc": "Отчество 1",
                "phone": "+11111111111"
            }
        }

patch_invalid_coords_payload = {
            "user": {
                "email": "user1@mail.ru",
                "fam": "Фамилия 1",
                "name": "Имя 1",
                "otc": "Отчество 1",
                "phone": "+11111111111"
            },
            "coords": {
                "height": "abc",
                "latitude": "null",
                "longtitude": "null"
              }
        }

patch_non_new_status_payload = {
            "title": "Changed Title",
            "user": {
                "email": "user3@mail.ru",
                "fam": "Фамилия 3",
                "name": "Имя 3",
                "otc": "Отчество 3",
                "phone": "+33333333333"
            }
        }
