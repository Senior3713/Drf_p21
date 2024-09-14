from unicodedata import category

import graphene
from graphene import Argument
from graphene_django import DjangoObjectType

from apps.models import Product, Category


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, name):
        category = Category.objects.create(
            name=name
        )
        return CreateCategory(category=category)


class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    msg = graphene.String()

    def mutate(self, info, id):
        Category.objects.get(id=id).delete()
        return DeleteCategory(msg="o'chirildi")


class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        slug = graphene.String()

    msg = graphene.String()

    def mutate(self, info, id, **kwargs):
        Category.objects.filter(id=id).update(**kwargs)

        return UpdateCategory(msg="Successfully updated!")


class Query(graphene.ObjectType):
    products = graphene.List(
        ProductType,
        page=graphene.Int(),
        page_size=graphene.Int()
    )

    categories = graphene.List(CategoryType, description='Bu kategoriya hisoblanadi')


    def resolve_products(self, info, page=None, page_size=3):
        qs = Product.objects.all()
        if page and page_size:
            qs = qs[(page-1)*page_size: page*page_size]
        return qs

    def resolve_categories(self, info):
        return Category.objects.all()


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    delete_category = DeleteCategory.Field()
    update_category = UpdateCategory.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
