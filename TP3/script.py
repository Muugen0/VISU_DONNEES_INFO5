def uneDecomposition(data):
    new_data = []
    coeff = []
    for i in range(0, len(data)-1, 2):
        moyenne = (data[i]+data[i+1])/2
        new_data.append(moyenne)
        coeff.append(data[i]-moyenne)
    return new_data,coeff

def uneRecomposition(data, coeff):
    new_data = []
    for i in range(len(data)):
        new_data.append(data[i] + coeff[i])
        new_data.append(data[i] - coeff[i])
    return new_data

def Decomposition(data):
    new_data = data
    coeff = []
    while len(new_data) > 1:
        new_data,new_coeff = uneDecomposition(new_data)
        coeff.insert(0, new_coeff)
    return new_data,coeff

def Recomposition(data, levels):
    new_data = data
    
    for coeff in levels:
        new_data = uneRecomposition(new_data, coeff)
    
    return new_data

data = [9.0,7.0,3.0,5.0,2.0,10.0,8.0,12.0]
print("initial data : ", data)
data_decomposition,coeff = uneDecomposition(data)
print("new data : ", data_decomposition)
print("coeff : ", coeff)
data_recomposition = uneRecomposition(data_decomposition, coeff)
print("data recomposition : ", data_recomposition)
print("---------------------------------------------------------")
print("initial data : ", data)
data_decomposition,coeff = Decomposition(data)
print("new data : ", data_decomposition)
print("coeff : ", coeff)
data_recomposition = Recomposition(data_decomposition, coeff)
print("data recomposition ; ", data_recomposition)
