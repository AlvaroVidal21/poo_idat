class producto():

    # Atributos Encapsulados (Privados)
    __codigoProducto = ""; __nombreProducto = ""
    __descripcionProducto = ""; __stockMinimoProducto = ""
    __stockActualProducto = ""; __precioCostoProducto = ""
    __precioVentaProducto = ""; __proveedorProducto = ""
    __almacenProducto = ""

    # Constructor
    def __init__(self, codigoProducto, nombreProducto, descripcionProducto,
                 stockMinimoProducto, stockActualProducto,
                 precioCostoProducto, precioVentaProducto,
                 proveedorProducto, almacenProducto):
        self.__codigoProducto = codigoProducto
        self.__nombreProducto = nombreProducto
        self.__descripcionProducto = descripcionProducto
        self.__stockMinimoProducto = stockMinimoProducto
        self.__stockActualProducto = stockActualProducto
        self.__precioCostoProducto = precioCostoProducto
        self.__precioVentaProducto = precioVentaProducto
        self.__proveedorProducto = proveedorProducto
        self.__almacenProducto = almacenProducto

    def getCodigoProducto(self):
        return self.__codigoProducto
    def setCodigoProducto(self, codigoProducto):
        self.__codigoProducto = codigoProducto

    def getNombreProducto(self):
        return self.__nombreProducto
    def setNombreProducto(self, nombreProducto):
        self.__nombreProducto = nombreProducto

    def getDescripcionProducto(self):
        return self.__descripcionProducto
    def setDescripcionProducto(self, descripcionProducto):
        self.__descripcionProducto = descripcionProducto

    def getStockMinimoProducto(self):
        return self.__stockMinimoProducto
    def setStockMinimoProducto(self, stockMinimoProducto):
        self.__stockMinimoProducto = stockMinimoProducto

    def getStockActualProducto(self):
        return self.__stockActualProducto
    def setStockActualProducto(self, stockActualProducto):
        self.__stockActualProducto = stockActualProducto

    def getPrecioCostoProducto(self):
        return self.__precioCostoProducto
    def setPrecioCostoProducto(self, precioCostoProducto):
        self.__precioCostoProducto = precioCostoProducto

    def getPrecioVentaProducto(self):
        return self.__precioVentaProducto
    def setPrecioVentaProducto(self, precioVentaProducto):
        self.__precioVentaProducto = precioVentaProducto

    def getProveedorProducto(self):
        return self.__proveedorProducto
    def setProveedorProducto(self, proveedorProducto):
        self.__proveedorProducto = proveedorProducto

    def getAlmacenProducto(self):
        return self.__almacenProducto
    def setAlmacenProducto(self, almacenProducto):
        self.__almacenProducto = almacenProducto

    # utilidades para trabajar con archivos CSV
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["codigo"],
            data["nombre"],
            data["descripcion"],
            data["stock_minimo"],
            data["stock_actual"],
            data["precio_costo"],
            data["precio_venta"],
            data["proveedor"],
            data["almacen"],
        )

    def to_dict(self):
        return {
            "codigo": self.getCodigoProducto(),
            "nombre": self.getNombreProducto(),
            "descripcion": self.getDescripcionProducto(),
            "stock_minimo": self.getStockMinimoProducto(),
            "stock_actual": self.getStockActualProducto(),
            "precio_costo": self.getPrecioCostoProducto(),
            "precio_venta": self.getPrecioVentaProducto(),
            "proveedor": self.getProveedorProducto(),
            "almacen": self.getAlmacenProducto(),
        }

