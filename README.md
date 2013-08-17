python-nutritionix
==================

Nutritionix API Python wrapper

![Nutritionix API Credit](https://d3jpl91pxevbkh.cloudfront.net/nutritionix/image/upload/v1363458498/attribution_jqfdgy.png)


Installing
==========

`pip install nutritionix`

Dependencies
------------

Requires [Requests](http://docs.python-requests.org/en/latest/).


Config
======

You'll need an api key and app id which is tied to a developer account at
https://developer.nutritionix.com

You may provide these parameters in your code or with the environment variables
`NIX_APP_ID` &amp; `NIX_API_KEY`


Usage
=====

#### Instantiate ####

First, instantiate the API wrapper object

    from nutritionix import Nutrtionix
    nix = Nutritionix(app_id="123456789", api_key="XXXYYYZZZ")

Or if you have configured the environment variables, simply

    from nutritionix import Nutrtionix
    nix = Nutritionix()

#### Define request ####

Defining a request is simply chaining a method to the API wrapper instance

    pizza = nix.search("pizza")

That will return a new wrapper object which will perform a search for pizza.

#### Retrieve results ####

We can retrieve the parsed JSON results easily by using the json method

    results = pizza.json()

All of this could also be written more concisely as

    nix.search('pizza').json()

#### Using parameters ####

Of course adding parameters is easy- just pass them as keyword arguments
to the method

    nix.search('pizza', results="0:1").json()


Examples
========

### Search ###

    >>> nix.search("big mac", results="0:1").json()
    {u'hits': [{u'_id': u'513fc9e73fe3ffd40300109f',
                u'_index': u'nixProductionV9',
                u'_score': 1.1813704,
                u'_type': u'item',
                u'fields': {u'brand_name': u"McDonald's",
                            u'item_id': u'513fc9e73fe3ffd40300109f',
                            u'item_name': u'Big Mac'}}],
     u'max_score': 1.1813704,
     u'total_hits': 1050}

### Items ###

    >>> nix.item(id="513fc9e73fe3ffd40300109f").json()
    {u'allergen_contains_eggs': None,
     u'allergen_contains_fish': None,
     u'allergen_contains_gluten': None,
     u'allergen_contains_milk': None,
     u'allergen_contains_peanuts': None,
     u'allergen_contains_shellfish': None,
     u'allergen_contains_soybeans': None,
     u'allergen_contains_tree_nuts': None,
     u'allergen_contains_wheat': None,
     u'brand_id': u'513fbc1283aa2dc80c000053',
     u'brand_name': u"McDonald's",
     u'item_description': u'7.6 oz (215 g)',
     u'item_id': u'513fc9e73fe3ffd40300109f',
     u'item_name': u'Big Mac',
     u'leg_loc_id': 114,
     u'nf_calcium_dv': 25,
     u'nf_calories': 550,
     u'nf_calories_from_fat': 260,
     u'nf_cholesterol': 75,
     u'nf_dietary_fiber': 3,
     u'nf_ingredient_statement': u'100% Beef Patty...',
     u'nf_iron_dv': 25,
     u'nf_monounsaturated_fat': None,
     u'nf_polyunsaturated_fat': None,
     u'nf_protein': 25,
     u'nf_refuse_pct': None,
     u'nf_saturated_fat': 10,
     u'nf_serving_size_qty': 1,
     u'nf_serving_size_unit': u'Burger',
     u'nf_serving_weight_grams': 215,
     u'nf_servings_per_container': None,
     u'nf_sodium': 970,
     u'nf_sugars': 9,
     u'nf_total_carbohydrate': 46,
     u'nf_total_fat': 29,
     u'nf_trans_fatty_acid': 1,
     u'nf_vitamin_a_dv': 4,
     u'nf_vitamin_c_dv': 2,
     u'nf_water_grams': None,
     u'old_api_id': None,
     u'updated_at': u'2013-06-28T17:53:50.000Z'}


### Brands ###

    >>> nix.brand("513fbc1283aa2dc80c000053").json()
    {u'brand_id': u'513fbc1283aa2dc80c000053',
     u'created_at': u'2011-07-01 08:45:47',
     u'name': u"McDonald's",
     u'old_api_id': u'0PewL8juRBSozVk',
     u'type': 1,
     u'updated_at': u'2013-06-26T11:36:25.468Z',
     u'website': u'http://www.mcdonalds.com'}

Todo
====

+ Add NXQL support
