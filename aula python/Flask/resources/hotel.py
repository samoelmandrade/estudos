from flask_restful import Resource, reqparse


hoteis =[
    
        { 'hotel_id':'01',
          'Novo':'campo'
        },
        {'hotel_id':'02',
         'Novo':'campo2'
         },
        {'hotel_id':'03',
         'Novo':'campo3'
         }  
    
]

class Hoteis(Resource):
    def get(self):
        return hoteis

class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
            
        return{'message: hotel not found'},404
    
    def post(self, hotel_id):
        argumentos = reqparse.RequestParser()
        print(argumentos)
        argumentos.add_argument('Novo')
        
        dados= argumentos.parse_args()
        novo_hotel = {
            'hotel_id': hotel_id,
            'Novo':dados['Novo']
        }
        hoteis.append(novo_hotel)
        return novo_hotel,200
    
    
    def put(self, hotel_id):
        pass
    def delete(self, hotel_id):
        pass