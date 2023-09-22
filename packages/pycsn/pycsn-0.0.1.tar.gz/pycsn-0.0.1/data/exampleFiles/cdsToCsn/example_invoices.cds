/* Test entities with a simplified relational model for illustrating the syntax of CDS, CSN, ... */

namespace test.supplier.invoices;

entity Company {
  key COMPANY_ID:       String(10);
  NAME:                 String;
  COUNTRY:              String;
  /* managed to-many association */
  SENT_INVOICES:        Association to many Invoice
                          on SENT_INVOICES.BILL_FROM = $self;
  /* managed to-many association */
  RECEIVED_INVOICES:    Association to many Invoice
                          on RECEIVED_INVOICES.BILL_TO = $self;
}

entity Invoice {
  /* managed to-one association providing the backlink to the managed to-many association */
  key BILL_FROM:        Association to Company;
  key INVOICE_NUMBER:   Integer;
  /* managed to-one association providing the backlink to the managed to-many association */
  BILL_TO:              Association to Company;
  INVOICE_DATE:         Date;
  DUE_DATE:             Date;
  CURRENCY:             String(3);
  ITEMS:                Composition of many InvoiceItem
                          on ITEMS.INVOICE = $self;
}

entity Service {
  key SERVICE_ID:       Integer;
  SERVICE_NAME:         String(100);
  /* managed to-many association */
  INVOICE_ITEMS:        Association to many InvoiceItem
                          on INVOICE_ITEMS.SERVICE = $self;
}

entity InvoiceItem {
  /* managed to-one association providing the backlink to the composition */
  key INVOICE:        Association to Invoice;
  key ITEM_ID:        Integer;
  /* managed to-one association providing the backlink to the managed to-many association */
  SERVICE:            Association to Service;
  AMOUNT:             Decimal(20, 2);
}

entity viewBillerInvoiceHeaders as SELECT
    from Invoice { BILL_FROM.COMPANY_ID as SupplierId,
    INVOICE_NUMBER as InvoiceNumber,
    BILL_TO.COMPANY_ID as ReceiverId,
    DUE_DATE as DueDate,
    SUM(ITEMS.AMOUNT) as InvoiceAmount,
    CURRENCY as InvoiceCurrency }
    GROUP BY BILL_FROM.COMPANY_ID, INVOICE_NUMBER;
