from django.db import models


# Create your models here.
class Herb(models.Model):
    scientific_name = models.CharField(max_length=50, unique=True)
    vietnamese_name = models.CharField(max_length=50, unique=True)
    familia = models.CharField(max_length=50, null=True)
    vietnamese_synonyms = models.CharField(max_length=150, null=True)
    stem = models.CharField(max_length=300, null=True)
    root = models.CharField(max_length=300, null=True)
    leaf = models.CharField(max_length=300, null=True)
    flower = models.CharField(max_length=400, null=True)
    fruit = models.CharField(max_length=200, null=True)
    image0 = models.CharField(max_length=200, null=True)
    image1 = models.CharField(max_length=200, null=True)
    image2 = models.CharField(max_length=200, null=True)
    image3 = models.CharField(max_length=200, null=True)
    image_ref = models.CharField(max_length=200, null=True)
    time = models.DateField(null=True)
    def __str__(self):
        return '%s' % (self.vietnamese_synonyms)


class Compound(models.Model):
    iupac_name = models.CharField(max_length=400)
    synonym = models.CharField(max_length=100, unique=True)
    formula = models.CharField(max_length=200, null=True)
    structure = models.CharField(max_length=200, null=True)
    pubchem_ref = models.CharField(max_length=150, null=True)
    can_smiles = models.CharField(max_length=250, null=True)
    iso_smiles = models.CharField(max_length=250, null=True)
    herb = models.ManyToManyField(Herb)


class Target(models.Model):
    protein_name = models.CharField(max_length=100, unique=True)
    gene_name = models.CharField(max_length=100)
    uniprot_ref = models.CharField(max_length=100, null=True)
    uniprot_code = models.CharField(max_length=50, null=True)
    herb = models.ManyToManyField(Herb)
    compound = models.ManyToManyField(Compound)

class Disease(models.Model):
    disease_name_en = models.CharField(max_length=100, unique=True)
    icd10_ref_en = models.CharField(max_length=200)
    icd10_code_en = models.CharField(max_length=50)
    disease_name_vn = models.CharField(max_length=100)
    icd10_ref_vn = models.CharField(max_length=200)
    icd10_code_vn = models.CharField(max_length=50)