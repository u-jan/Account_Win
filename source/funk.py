import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats



def seaborn_count_barplot_won(df,col_name):
    print(f'Winner customers(Won = 1): {round((df[col_name].sum() / df.shape[0]) *100,1)}%')
    print(f'Other customers (Won = 0): {round((1 - (df[col_name].sum() / df.shape[0])) * 100,1)}%')
    print(f'Number of (Won = 1): {round((df[col_name].sum() / df.shape[0]) * df.shape[0])}')
    print(f'Number of  (Won = 0): {round((1 - (df[col_name].sum() / df.shape[0])) *df.shape[0])}')
    counts = df[col_name].value_counts()
    sns.barplot(counts.index, counts)
    
def seaborn_count_barplot(df,col_name):
    counts = df[col_name].value_counts()
    sns.barplot(counts.index, counts)

    
def title_ranks(x):
    rank_1 = ['President','ceo','Partner','Co_founder','founder','Founder','Chairman','Owner','president','PRESIDENT','FOUNDER','Board']
    rank_2 = ['VP','Executive','Lead','GM','Director','Head','head','Principal','Coo','General','Exec','VC']
    rank_3 = ['manager','Managing','Manager','managing','Senior','senior','sr','Sr','Chief','manger']
    
    
    if ('C' in x and 'O'in x):
        return 'rank_1'
    
    for c in rank_1:
        if c in x:
            return 'rank_1'
        
    for c in rank_2:
        if c in x:
            return 'rank_2'
        
    for c in rank_3:
        if c in x:
            return 'rank_3'
    
    if x == '-1':
        return "rank_unknown"
    
    else:
        return 'rank_4'

    
    
    
    
    
def plt_barplot(df,col_name):
    rank_count  = df[col_name].value_counts()
    # rank_count = rank_count[:10,]
    plt.figure(figsize=(10,5))
    sns.barplot(rank_count.index, rank_count.values, alpha=0.8)
    plt.title(f'{col_name} Counts')
    plt.ylabel('Number of Occurrences', fontsize=12)
    plt.xlabel(f'{col_name}', fontsize=12)
    plt.xticks(rotation=55)
    plt.show()
    
def binary_behaviour_with_numbers(df,target,col_name):
    cross = pd.crosstab(df[target], df[col_name], rownames=[target])
    print(cross)
    (cross / cross.apply(sum)).plot(kind="bar",figsize= (10,5), sort_columns = False)
    plt.show()
    
def binary_behaviour(df,target,col_name):
    cross = pd.crosstab(df[target], df[col_name], rownames=[target])
    (cross / cross.apply(sum)).plot(kind="bar")
    plt.show()
    

def binary_behaviour_with_large_numbers(df,target,col_name):
    cross = pd.crosstab(df[target], df[col_name], rownames=[target])
    #print(cross)
    (cross / cross.apply(sum)).plot(kind="bar",figsize= (20,5), sort_columns = False)
    plt.show()
    
    
    
def one_hot_dummy(input_df, columns):
    df_hot = input_df.copy()

    for col in columns:
        dummies = pd.get_dummies(df_hot[col])
#         dummies.drop(dummies.columns[-1], axis=1, inplace=True)  --> not my tempo
        df_hot = df_hot.drop(col, axis=1).merge(dummies, left_index=True, right_index=True)
    
    return df_hot


def heatmap(df, columns):
    
    df = one_hot_dummy(df,columns)

    from string import ascii_letters
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.set(style="white")


    # Compute the correlation matrix
    corr = df.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    
    
    
    
    
    

def title_job_category(x):
    HR = ['HR','hr','resource','Re','talent','Talent','Team']
    Sales_Marketing = ['sales','sale','Sales','market','Market','MARKET','SALE','Principal','Coo','General','Exec','VC','CM']
    business_dev = ['deve','Deve','BD','bd','Bd']
    consulting = ['consul','Consul','Cont']
    finance = ['finance','Finance','CFO','cfo']
    customer_succes = ['succes','client','Client','customer','Customer']
    tech = ['CTO']
    project_manager = ['PM','project','Project','Tech','tech']
    product = ['product','Product']
    founder_ceo_owner = ['CEO','ceo','Partner','Co_founder','founder','Founder','Chairman','Owner','president','PRESIDENT','FOUNDER','Board','President','Founding','founding']
    operations = ['coo','COO','operations','Operations','ops']
    office = ['office','Office']
    culture = ['culture','Culture','People','people','CRO','staff']
    admin_manager = ['manager','Manager','Admin','admin','management','Management','GM','Head','HEAD','Director']
    
    
    # no offense, I certainly know sales and marketing professionals have different job descriptions and skills
    # however we are dealing with a lot of C-level execitives here, in which some deals with both professions. so I grouped them.
    
#     rank_3 = ['manager','Managing','Manager','managing','Senior','senior','sr','Sr','Chief','manger']
    
    
#     if ('C' in x and 'O'in x):
#         return ''

    for c in HR:
        if c in x:
            return 'HR'
        
    for c in Sales_Marketing:
        if c in x:
            return 'S & M'

    for c in business_dev:
        if c in x:
            return 'BD'

    for c in consulting:
        if c in x:
            return 'Consulting'
        
    for c in finance:
        if c in x:
            return 'Finance'
        
    for c in customer_succes:
        if c in x:
            return 'CLS'
        
    for c in tech:
        if c in x:
            return 'Tech'
    
    for c in project_manager:
        if c in x:
            return 'Project'

    for c in product:
        if c in x:
            return 'Product'
        
    for c in founder_ceo_owner:
        if c in x:
            return 'Owner_Ceo'
    for c in operations:
        if c in x:
            return 'OPS'
    for c in office:
        if c in x:
            return 'Office'
    for c in culture:
        if c in x:
            return 'Culture'
    for c in admin_manager:
        if c in x:
            return 'Manager'

    if x == '-1':
        return "n/a"
    
    else:
        return 'Other'

    
    
# for the donut.
def lead_group_donut(x):
    if 'MKTG' in x:
        return ' MKTG'
    elif 'Google' in x and 'MKTG' not in x:
        return 'Google'
    elif x == 'Existing Customer':
        return x
    elif ('Referral' in x and 'MKTG' not in x) or ('Referral' in x and 'Google' not in x):
        return 'Referral'
    else:
        return 'Other'

def group_size(df):
    MKTG = []
    Google = []
    Existing_Customer = []
    Referral = []
    Others = []

    group_names= ['MKTG', 'Google', 'Existing Customer','Referral','Others']
    group_list = [MKTG,Google,Existing_Customer, Referral, Others]

    group_size = [size for size in df.lead_group.value_counts()]
    return group_names,group_size



def outter_donut(df,group,groupsize):
    group_names,group_size = group,groupsize

    group_names_with_count = []
    for i in range(len(group_names)):
        group_names_with_count.append(group_names[i] + " : " + f'{group_size[i]}')
    
    
    
        # reate colors
    a, b, c, d, e =[plt.cm.Blues, plt.cm.Reds, plt.cm.Greens, plt.cm.Oranges, plt.cm.twilight_shifted]

    # First Ring (outside)
    fig, ax = plt.subplots()
    ax.axis('equal')
    mypie, _ = ax.pie(group_size, radius=1.3*2, labels=group_names_with_count, colors=[a(0.6), b(0.6), c(0.6),d(0.6), e(0.6)] )
    plt.setp( mypie, width=0.3*2, edgecolor='white')

    # Second Ring (Inside)
    # mypie2, _ = ax.pie(subgroup_size, radius=(1.3-0.3)*2, labels=subgroup_names, labeldistance=0.7, colors=[a(0.5), a(0.4), a(0.3), b(0.5), b(0.4), c(0.6), c(0.5), c(0.4), c(0.3), c(0.2)])
    # plt.setp( mypie2, width=0.4*2, edgecolor='white')
    # plt.margins(0,0)

    # show it
    plt.show()


    
def industry_group(df,col_name):

    industries = []
    for c in df[col_name].values:
        if c != -1:
            if df.Industry.value_counts()[f'{c}'] > 20:
                industries.append(c)

            else:
                industries.append('others')
        else:
            industries.append('n/a')
        
    df['industry_groups'] = industries
    return df

    
    
    
def barplot_vs(df,col_name,target_name):
    df_visul = df[[target_name,col_name]]
    
    fig, (ax1) = plt.subplots(ncols=1, sharey=True,figsize=(15,5))
    fig.suptitle(f'{col_name} Counts')
    g1 = sns.countplot(x=f'{col_name}',
                      hue= target_name, data= df_visul, ax=ax1, order= list(df[col_name].value_counts().keys()))

    # g2 = sns.countplot(x='industry_groups',
    #                   hue='Won', data=df_industry_visul, ax=ax2, order= orderly)
    # plt.figure(figsize=(10,5))
    g1.legend_.remove()
    plt.legend(bbox_to_anchor=(0.9, 1), loc=2, borderaxespad=1., title='Won')
    g1.set_xlabel(f'# {col_name}')
    plt.xticks(rotation=45)
    plt.show()
    
    
def barplot_double_vs(df,col_name,col_2_name,target_name):
    df_visul = df[[target_name,col_name,col_2_name]]
    
    fig, (ax1,ax2) = plt.subplots(ncols=2, sharey=True,figsize=(15,5))
    fig.suptitle(f'{col_name} Counts')
    g1 = sns.countplot(x=f'{col_name}',
                      hue= target_name, data= df_visul, ax=ax1, order= list(df[col_name].value_counts().keys()))

    g2 = sns.countplot(x=f'{col_2_name}',
                      hue= target_name, data= df_visul, ax=ax2, order= list(df[col_2_name].value_counts().keys()))

    g1.legend_.remove()
    plt.legend(bbox_to_anchor=(0.9, 1), loc=2, borderaxespad=1., title='Won')
    g1.set_xlabel(f'# {col_name}')
    g2.set_xlabel(f'# {col_2_name}')
    g2.set_ylabel('')
    plt.xticks(rotation=45)
    plt.show()
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def amount_it(x):
    y = ''
    if x != -1:
        x = x[1:len(x)-3]
        
        for c in x:
            if c != ',':
                y += c
        return int(y)
                
    else:
        return x


def amount_groups(df,x):
    linspace = np.linspace(min(df.Amount),max(df.Amount)*0.8,100)
    if x >= 0:
        for i in range(len(linspace)-1):
            if x > linspace[i] and x < linspace[i+1]:
                return round(linspace[i])
            elif x > max(df.Amount)*0.8:
                return max(df.Amount)*0.8
        

    else:
        return x

    
    
def registered_days_fill_median(x):
    if x < 0:
        return 
    
    
    
    