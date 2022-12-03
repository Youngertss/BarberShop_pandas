import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel(open('dataset_bs.xlsx', 'rb'))
print(df.info())
#df[df["рейтинг"]==5]["вместимость"].plot(kind="barh",grid=True,title="Вместимость у БШ с 5 рейтинга")
df[df["ценовая категория"]=="высше среднего"]["вместимость"].plot(kind="bar",grid=True,title="Вместимость БШ с цен. категорией\nвыше среденго")
plt.show()

        #Наличие сайта
#print(df[(df["наличие сайта"]=="Нету")]["рейтинг"].mean())
#print(df[(df["наличие сайта"]=="Есть")]["рейтинг"].mean())

        #Качевство иструментов
#print(df[(df["качество иструментов"]>=7)]["рейтинг"].mean())
#print(df[(df["качество иструментов"]<7)]["рейтинг"].mean())
#print(df[(df["качество иструментов"]==8) & (df['ценовая категория']=="средний")]["рейтинг"].mean())
#print(df[(df["качество иструментов"]==8) & (df['ценовая категория']=="высше среднего")]["рейтинг"].mean())

        #Рейтинг и качество инструметов с цен кат
#print(df[(df["ценовая категория"]=="средний")]["рейтинг"].mean())
#print(df[(df["ценовая категория"]=="средний")]["качество иструментов"].mean())
#print(df[(df["ценовая категория"]=="высше среднего")]["рейтинг"].mean())
#print(df[(df["ценовая категория"]=="высше среднего")]["качество иструментов"].mean())

        #Кол-во услуг
#print(df[(df["кол-во услуг"]>6)]["рейтинг"].mean())
#print(df[(df["кол-во услуг"]<=6)]["рейтинг"].mean())
    
        #Название
#print(df[(df["рейтинг"]==df['рейтинг'].max())]['название'])
#print(df[(df["рейтинг"]==df['рейтинг'].min())]['название'])

    #Вместимость
#print(df[(df["рейтинг"]==df['рейтинг'].max())]['вместимость'].mean())
#print(df[(df["рейтинг"]==df['рейтинг'].min())]['вместимость'].mean())
#print(df[(df["вместимость"]==7)]["рейтинг"].mean())

    #Колво точек
#print(df[(df["рейтинг"]==df['рейтинг'].max())]['кол-во точек'].mean())
#print(df[(df["рейтинг"]==df['рейтинг'].min())]['кол-во точек'].mean())
#print(df[(df["ценовая категория"]=="высше среднего")]["кол-во точек"].mean())


