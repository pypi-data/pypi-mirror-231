import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
def enrichment_dotplot(enrich_results, n=20, hue='Z-score', scheme="Blues", log=True):
    """
    Plots enrichment results in dotplot form
    
    Parameters
    ----------
    enrich_results: pd.DataFrame
      - result dataframe from enrichrpy.enrichr.get_pathway_enrichment
    n: int
      - plot top N pathways, default=20
    hue: str
      - variable to color the dotplot by, default='Combined score'
    scheme: str
      - seaborn color scheme to use.
    """
    df = enrich_results.copy()
    df['Num hits'] = [len(ls) for ls in df['Overlapping genes']]
    df['-log10(Adjusted p-value)'] = -np.log10(df['Adjusted p-value'])
    df['Pathway'] = df['Term name'].to_list()
    df[f'log({hue})'] = np.log(df[hue])
    
    if n is not None:
        data= df.sort_values('Adjusted p-value').iloc[:n]  
        import matplotlib.pyplot as plt
        import seaborn as sns
        plt.figure(figsize=(4,6))
        sns.scatterplot(data=data, x="-log10(Adjusted p-value)", y="Pathway", hue="log(Z-score)",size="Num hits",palette=sns.color_palette(scheme,as_cmap=True),sizes=(40, 260),hue_norm=(1,10), legend="auto")#)#, style="time")
        plt.legend(loc='best',scatterpoints=1,labelspacing=1,markerscale=0.9,fontsize='small',bbox_to_anchor=(1.05,1.0),borderaxespad=0.,title_fontsize='large')#,scatteryoffsets=1
        plt.axvline(1,color="red",linestyle="--",linewidth=2)
        plt.xticks(np.arange(0, 15, step=2))
        plt.show()
    