import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import cv2
import os


def createDataFrame()->pd.DataFrame:
    '''This function takes data from 2 csv files and create dataframe with 2 columns'''
    annotation1 = pd.read_csv(os.path.join("D:\\","PP_lab2","PP_lab2","annotation1.csv"), sep=' ',
                      header=None, encoding='UTF-16')
    annotation2 = pd.read_csv(os.path.join("D:\\","PP_lab2","PP_lab2","annotation2.csv"), sep=' ',
                      header=None, encoding='UTF-16')
    df = pd.concat([annotation1, annotation2], ignore_index=True)
    df.drop(1, axis=1, inplace=True)
    df.rename(columns={0: 'AbsolutePath', 2: 'DatasetClass'}, inplace=True)
    return df


def add_mark(df: pd.DataFrame) -> None:
    '''This function adds third column in dataframe - mark of image(1 or 0)'''
    index = []
    for item in df['DatasetClass']:
        if item == 'bayhorse':
            index.append(0)
        else:
            index.append(1)
    df['mark'] = index


def add_parametrs(df: pd.DataFrame) -> None:
    '''This function adds to dataframe 3 columns: height, width and channels of the image'''
    imagewidth = []
    imageheight = []
    imagechannel = []
    for item in df['AbsolutePath']:
        img = cv2.imread(item)
        imageheight.append(img.shape[0])
        imagewidth.append(img.shape[1])
        imagechannel.append(img.shape[2])
    df['height'] = imageheight
    df['width'] = imagewidth
    df['channel'] = imagechannel


