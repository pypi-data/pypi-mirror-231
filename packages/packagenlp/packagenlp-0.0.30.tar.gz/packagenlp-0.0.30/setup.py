import setuptools

setuptools.setup(
    name="packagenlp",
    packages=['packagenlp'],
    version="0.0.30",
    author="Business & Décision",
    description="A package for NLP",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["NLP", "Français", "Langues", "Traitements"],
    download_url="https://gitlab.com/business-decision-data-science/packagenlp/-/package_files/82622627/download",
    python_requires='>=3.6',
    install_requires=[
        'pandas',
        'nltk',
        'spacy',
        'unidecode',
        'treetaggerwrapper',
        'streamlit',
        'plotly',
        'wordcloud'
    ],
    include_package_data=True,
    package_data={'': ['data/stopWords_spacy_en.csv', 'data/stopWords_spacy_fr.csv','data/image.jpg','data/Logo_B_D.png']},
) 
