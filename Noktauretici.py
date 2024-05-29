import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#*******************************************************************************************************************************************
def rastgele_koordinat_uret_ve_kaydet(nokta_sayisi,dosya_adi):
    x_koordinatlari=np.random.randint(0,1001,nokta_sayisi)
    y_koordinatlari = np.random.randint(0,1001,nokta_sayisi)
    df=pd.DataFrame({'X': x_koordinatlari,'Y': y_koordinatlari})
    df.to_excel(dosya_adi,index=False)

#*******************************************************************************************************************************************
def koordinatlari_oku(dosya_adi):
    df=pd.read_excel(dosya_adi)
    return df['X'],df['Y']

#*******************************************************************************************************************************************
def koordinatlari_ciz(x_koordinatlari,y_koordinatlari,ızgara_boyutu):
    plt.figure(figsize=(10,10))
    eksen_basina_ızgara=1000 // ızgara_boyutu
    renk_haritasi=plt.get_cmap('tab20')
    renkler=renk_haritasi(np.linspace(0,1,25))

    for i in range(eksen_basina_ızgara):
        for j in range(eksen_basina_ızgara):
            maske=(x_koordinatlari >= i * ızgara_boyutu) & (x_koordinatlari < (i+1) * ızgara_boyutu) & (y_koordinatlari >= j * ızgara_boyutu) & (y_koordinatlari < (j+1) * ızgara_boyutu)
            renk_indeksi = i * eksen_basina_ızgara+j  
            plt.scatter(x_koordinatlari[maske],y_koordinatlari[maske], color=renkler[renk_indeksi],s=10,alpha=0.6)

#*******************************************************************************************************************************************
    plt.xlim(0,1000)
    plt.ylim(0,1000)
    plt.xlabel('X Koordinatları')
    plt.ylabel('Y Koordinatları')
    plt.title(f'Rastgele Nokta Haritası')
    plt.grid(True)
    plt.show()

#*******************************************************************************************************************************************
nokta_sayisi=1000
dosya_adi='koordinatlar.xlsx'
ızgara_boyutu=200 

#*******************************************************************************************************************************************
rastgele_koordinat_uret_ve_kaydet(nokta_sayisi,dosya_adi)
x_koordinatlari,y_koordinatlari=koordinatlari_oku(dosya_adi)
koordinatlari_ciz(x_koordinatlari,y_koordinatlari,ızgara_boyutu)
#*******************************************************************************************************************************************