from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import numpy as np
import pandas as pd

class CustomNumericalTransformer_rl(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass


    def fit(self, X, y=None):
        return self

    def transform(self, X):
        """
        Transforma los datos aplicando la lógica personalizada.
        """


        X["prbm_payerSalesSegment"]=np.where(X["payerSalesSegment"].isin([6]),0.002391,
        np.where(X["payerSalesSegment"].isin([5]),0.020237,
        np.where(X["payerSalesSegment"].isin([3,4]),0.117108,0.190335
        )))

        X['amountFinanced']=np.where(X['amountFinanced'].isnull(),713881,X['amountFinanced'])
        X["amountFinanced_log_abs"]= np.sign(X['amountFinanced']) * np.log(np.abs(X['amountFinanced']) + 1)
        X["amountFinanced_log_abs_cap"]=X["amountFinanced_log_abs"].clip(lower=0, upper=22)

        X['date']=pd.to_datetime(X['date'])
        X['paymentDate']=pd.to_datetime(X['paymentDate'])
        X['fecha_observacion']=pd.to_datetime(X['fecha_observacion'])
        X['expirationDate']=pd.to_datetime(X['expirationDate'])

        X['paymentDays'] = np.where(X['paymentDate'].isnull(),(X['fecha_observacion'] - X['expirationDate']).dt.days, # fecha de corte "foto"
                                    (X['paymentDate'] - X['expirationDate']).dt.days)
        
        X["prbm_paymentDays"]=np.where(X["paymentDays"]<=2,0.008933,
        np.where(X["paymentDays"]<=32,0.024220,
        np.where(X["paymentDays"]<=49,0.106759,
        np.where(X["paymentDays"]<=63,0.160494,
        np.where(X["paymentDays"]<=93,0.343100,0.733679
        )))))
        


        X['expirationDays'] = (X['expirationDate'] - X['date']).dt.days
        X["expirationDays_log_abs"]= np.sign(X['expirationDays']) * np.log(np.abs(X['expirationDays']) + 1)
        X["expirationDays_log_abs_cap"]=X["expirationDays_log_abs"].clip(lower=1.79, upper=5.08)

        X['date_paymentDays']=X['expirationDays']+X['paymentDays']
        X["date_paymentDays_cap"]=X["date_paymentDays"].clip(lower=-7, upper=280)


        return X[['prbm_payerSalesSegment',
                'amountFinanced_log_abs_cap',
                'prbm_paymentDays',
                'expirationDays_log_abs_cap',
                'date_paymentDays_cap']]
    
class CustomCategoricalTransformer_rl(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass


    def fit(self, X, y=None):
        return self

    def transform(self, X):
        """
        Transforma los datos aplicando la lógica personalizada.
        """

        sector_1=['Laboratorios y Fabricación Productos Farmacéuticos', 'Aerolíneas',
       'Suministro de Agua', 'Combustibles y Gas', 'Servicios de Salud',
       'Seguros e Isapres', 'Medios de Comunicación', 'Quimicos y Maderas']
        
        sector_2=['Retail', 'Ganadería', 'Acuicultura y Pesca', 'Minería y Metales']
        sector_3=['Construcción Ingeniería e Infraestructura']
        sector_4=['Hoteles, Restaurantes y Ocio', 'Agricultura y Relacionados',
            'Telecomunicaciones', 'Mercados de Capitales', 'Transporte',
            'Envíos y Almacenamiento', 'Energía', 'Relacionados a Construccion']
        sector_5=['Comercio', 'Consumo Basico', 'Servicios',
            'Tecnología de la Información', 'Gobierno y Actividades Sociales',
            'Maquinaria y Equipo','Industria Automotriz']
        sector_6=['Educación', 'Construcción de Viviendas', 'Tabaco']

        X["prbm_sector"]=np.where(X["sector"].isin(sector_1),0.000409,
        np.where(X["sector"].isin(sector_2),0.002683,
        np.where(X["sector"].isin(sector_3),0.005458,
        np.where(X["sector"].isin(sector_4),0.023589,
        np.where(X["sector"].isin(sector_5),0.050891,
        np.where(X["sector"].isin(sector_6),0.259167,0.050239
        ))))))

        return X[['prbm_sector']]
    
class CustomNumericalTransformer_ml(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass


    def fit(self, X, y=None):
        return self

    def transform(self, X):
        """
        Transforma los datos aplicando la lógica personalizada.
        """

        X['date']=pd.to_datetime(X['date'])
        X['paymentDate']=pd.to_datetime(X['paymentDate'])
        X['fecha_observacion']=pd.to_datetime(X['fecha_observacion'])
        X['expirationDate']=pd.to_datetime(X['expirationDate'])
        X['paymentDays'] = np.where(X['paymentDate'].isnull(),(X['fecha_observacion'] - X['expirationDate']).dt.days, # fecha de corte "foto"
                                    (X['paymentDate'] - X['expirationDate']).dt.days)
        
        X['amountFinanced']=np.where(X['amountFinanced'].isnull(),713881,X['amountFinanced'])
        X['expirationDays'] = (X['expirationDate'] - X['date']).dt.days

        X['date_paymentDays']=X['expirationDays']+X['paymentDays']


        return X[['amountFinanced',
                'payerSalesSegment',
                'paymentDays',
                'expirationDays',
                'date_paymentDays']]