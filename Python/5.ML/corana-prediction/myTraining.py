# from dbm import dumb
import pandas as pd
import numpy as np
import pickle

def split_data(data,ratio):
    np.random.seed(42)
    shuffled=np.random.permutation(len(data))
    test_set_size=int(len(data)*ratio)
    test_indices=shuffled[:test_set_size]
    train_indices=shuffled[test_set_size:]
    return data.iloc[train_indices],data.iloc[test_indices]



if __name__=='__main__':
    df=pd.read_csv('data.csv')
    train,test=split_data(df,0.2)
    X_train=train[['fever','bodypain','age','runny_noise','difficulty_in_breath']].to_numpy()
    X_test=test[['fever','bodypain','age','runny_noise','difficulty_in_breath']].to_numpy()
    Y_train=train[['infection_prob']].to_numpy().reshape(2000,)
    Y_test=test[['infection_prob']].to_numpy().reshape(499,)
    # now train model
    from sklearn.linear_model import LogisticRegression
    clf=LogisticRegression()
    clf.fit(X_train,Y_train)
    file=open('modal.pkl','wb')
    pickle.dump(clf,file)
   