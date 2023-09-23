namespace test.deliveries;

entity Supplier {
  key ID   : Integer;
  name     : String;
  country  : String;
}

entity Material {
  key ID     : Integer;
  name       : String;
}

entity MaterialSupplier {
  key SupplierID : Integer;
  key MaterialID : Integer;
}

entity Delivery {
  key ID     : UUID;
  materialID : Integer;
  supplierID : Integer;
  amount     : Integer;
}


entity viewSuppliers as SELECT from Supplier { * };

entity viewMaterials as SELECT from Material {
    ID, name as MaterialName
};

entity viewMaterialsPerSupplier as
    SELECT
        ms.SupplierID as SupplierID,
        ms.MaterialID as MaterialID,
        s.name as SupplierName,
        s.country as SupplierCountry,
        m.name as MaterialName
    from MaterialSupplier as ms
    inner join Material as m on ms.MaterialID = m.ID
    inner join Supplier as s on ms.SupplierID = s.ID;


entity viewDeliveriesWithMaterialAndSupplier as
    SELECT
        d.ID as DeliveryId,
        d.amount as DeliveryAmount,
        m.name as MaterialName,
        s.ID as SupplierId,
        s.name as SupplierName
    from Delivery as d
    inner join
    Material as m on d.materialID = m.ID
    inner join
    Supplier as s on d.supplierID = s.ID;
