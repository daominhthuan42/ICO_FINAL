# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 02:46:23 2020

@author: COMPUTER
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import numpy as geek

def loadDataset2(path = "D:\\HK1_2019_2020\\FINAL_PROJECT\\FINAL_PROJECT\\ICOOmen_ML_Model-master\\dataset\\ico_data_final.csv"):    
    dataset = pd.read_csv(path)
    x= dataset.iloc[:, 1:-1].values 
    data_com = dataset.iloc[:,1:14].values
    #Lấy giá trị cột cuối
    y= dataset.iloc[:,13].values
    icoNames = dataset.iloc[:,0]
    feauteNames = list(dataset.columns[1:-1])
    return (feauteNames, x, y, icoNames, data_com)

def encodeData(x):
    enc = OneHotEncoder(categorical_features='all',
           handle_unknown='error', sparse=False)
    # Mã hóa one hot cho 4 4 trường dữ liệu ICO Date, ICO month launched and ICO country.
    encodedCategoryArray= enc.fit_transform(x[:,8:12])
    # Loại bỏ 4 trường dữ liệu đó từ dataset.
    allInputsExceptCategorical = np.delete(x, np.s_[8:12], axis=1)
    # Ghép các input còn lại với các trường mã hóa.
    encodedX = np.concatenate((allInputsExceptCategorical,encodedCategoryArray),axis=1)
    return encodedX

  
    
    
 
if __name__ == "__main__": 
    
    # ĐA CỘNG TUYẾN
    (featureNames, x, y, icoNames, data_com) = loadDataset2()
    x_onehot = encodeData(x)
    det = np.linalg.det(x_onehot.T @ x_onehot)    
    print("Determinant of the matrix is : ",round(det))


    
    
    b = geek.identity(len(x_onehot.T @ x_onehot)) 
    print("\nMatrix b : \n", b) 
    lamda = 0.0000041
    det = np.linalg.det(x_onehot.T @ x_onehot + lamda*b)    
    print("Determinant of the matrix is : ",round(det))
    
    
    
    # ONE HOT ENCODING   
    
    data = pd.DataFrame(x, columns= ['price_usd', 'price_btc', 'total_supply', 'market_cap_usd', 'available_supply', 'usd_raised', 'eth_price_launch',
                                        'btc_price_launch', 'ico_duration',
                                        'month','day','country'])  
  
    encode = data.iloc[:,8:12]       
    enc = OneHotEncoder(categorical_features='all',
           handle_unknown='error', sparse=False)
    encodedCategoryArray= enc.fit_transform(encode)
    cat_columns = ['0', '1', '2', '3', '5',
                   '7', '10', '12', '13', '14',
                   '15', '18', '21', '22', '23',
                   '25', '27', '28', '29', '30',
                   '31', '32', '33', '34', '35',
                   '36', '38', '39', '41', '42',
                   '46', '49', '50', '52', '54',
                   '57', '58', '60', '61', '62',
                   '65', '66', '67', '69', '71',
                   '79', '91', '104', '112', '125',
                   '364', '4', '5', '6', '7', '8',
                   '9', '10', '11', '12', '1',
                   '2', '3', '4', '5', '6',
                   '7', '8', '9', '10', '12',
                   '13', '14', '15', '16', '17',
                   '18', '19', '20', '21', '22',
                   '23', '24', '25', '26', '27',
                   '28', '29', '31', '2', '8',
                   '9', '10', '28', '29', '33',
                   '37', '39', '51', '54', '56',
                   '59', '61', '77', '78', '86',
                   '94', '104', '130', '141', '148',
                   '152', '155', '156', '180', '182',
                   '194', '195', '196', '197']
    encodedCategoryArray = pd.DataFrame(encodedCategoryArray, columns = cat_columns)
    dataNotEncode = data.iloc[:,0:8]
    dataNotEncode = pd.DataFrame(dataNotEncode)
    datasetAfterOneHotEncoding = pd.concat([dataNotEncode, encodedCategoryArray], axis = 1)






