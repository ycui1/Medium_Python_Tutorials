# class Product:
#     def __init__(self, name, sku):
#         self.name = name
#         self.sku = sku
#         self._short_name = name[:3]
#         self.__wacky_name = name[::-1]
#
#
# product = Product("Vacuum", 1001)
# product._short_name
# product._Product__wacky_name


class Product:
    maker: str
    upc_shared: int

    def __init__(self, name: str, sku: int):
        self.name = name
        self.sku = sku

    def get_annual_sales(self, year: int) -> float:
        return 2000

    @staticmethod
    def evaluate_sales(sales: list[float]) -> tuple[float, float]:
        sales_mean = 100.0
        sales_std = 17.7
        return sales_mean, sales_std

class Product:
    """
    A class to manage product-related data for the application.

    Attributes:
        name: str, the name of the product
        sku: int, the Stock-Keeping Unit number for the product

    Methods:
        get_annual_sales: get the annual sales data for a product
    """

    def __init__(self, name: str, sku: int):
        """
        Initialize a Product instance
        :param name: str, the product's name
        :param sku: int, the product's sku (stock-keeping unit) number
        :return None
        """
        pass

    def get_annual_sales(self, year: int) -> float:
        """
        Get the product's annual sales amount for the specified year
        :param year: int, the year for which you want to get the annual sales
        :return: float, the annual sales in dollars
        """
        pass


class Product:
    def __init__(self, name: str, sku: int):
        self.name = name
        self.sku = sku

    def __str__(self):
        return f"{self.name} (SKU: {self.sku})"

    def __repr__(self):
        # or return f"{self.__class__.__name__}({self.name!r}, {self.sku})"
        return f"Product({self.name!r}, {self.sku})"

