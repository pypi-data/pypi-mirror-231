CREATE TABLE test_supplier_invoices_Company (
  COMPANY_ID NVARCHAR(10),
  NAME NVARCHAR(5000),
  COUNTRY NVARCHAR(5000),
  PRIMARY KEY(COMPANY_ID)
);

CREATE TABLE test_supplier_invoices_Invoice (
  INVOICE_NUMBER INTEGER,
  INVOICE_DATE DATE,
  DUE_DATE DATE,
  CURRENCY NVARCHAR(3),
  BILL_FROM_COMPANY_ID NVARCHAR(10),
  BILL_TO_COMPANY_ID NVARCHAR(10),
  PRIMARY KEY(INVOICE_NUMBER, BILL_FROM_COMPANY_ID)
);

CREATE TABLE test_supplier_invoices_InvoiceItem (
  ITEM_ID INTEGER,
  AMOUNT DECIMAL(20, 2),
  INVOICE_BILL_FROM_COMPANY_ID NVARCHAR(10),
  INVOICE_INVOICE_NUMBER INTEGER,
  SERVICE_SERVICE_ID INTEGER,
  PRIMARY KEY(ITEM_ID, INVOICE_BILL_FROM_COMPANY_ID, INVOICE_INVOICE_NUMBER)
);

CREATE TABLE test_supplier_invoices_Service (
  SERVICE_ID INTEGER,
  SERVICE_NAME NVARCHAR(100),
  PRIMARY KEY(SERVICE_ID)
);

CREATE VIEW test_supplier_invoices_viewBillerInvoiceHeaders AS SELECT
  Company_1.COMPANY_ID AS SupplierId,
  Invoice_0.INVOICE_NUMBER AS InvoiceNumber,
  Company_2.COMPANY_ID AS ReceiverId,
  Invoice_0.DUE_DATE AS DueDate,
  SUM(InvoiceItem_3.AMOUNT) AS InvoiceAmount,
  Invoice_0.CURRENCY AS InvoiceCurrency
FROM (((test_supplier_invoices_Invoice AS Invoice_0
  LEFT JOIN test_supplier_invoices_Company AS Company_1
    ON (Invoice_0.BILL_FROM_COMPANY_ID = Company_1.COMPANY_ID))
  LEFT JOIN test_supplier_invoices_Company AS Company_2
    ON (Invoice_0.BILL_TO_COMPANY_ID = Company_2.COMPANY_ID))
  LEFT JOIN test_supplier_invoices_InvoiceItem AS InvoiceItem_3
    ON ((InvoiceItem_3.INVOICE_BILL_FROM_COMPANY_ID = Invoice_0.BILL_FROM_COMPANY_ID)
      AND (InvoiceItem_3.INVOICE_INVOICE_NUMBER = Invoice_0.INVOICE_NUMBER)))
GROUP BY Company_1.COMPANY_ID, Invoice_0.INVOICE_NUMBER
