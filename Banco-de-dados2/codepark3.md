# Banco de dados II - Codepark 3
***

>Uma empresa de vendas tem um banco de dados com informações sobre os seus produtos. Ela precisa criar um relatório que faça um levantamento diário da quantidade de produtos comprados por dia. Para ajudar a empresa, crie um procedure para agilizar esse processo.

#### Resposta
***

```
DELIMITER $$

CREATE PROCEDURE Verificar_Quantidade_Produtos(OUT quantidade INT)
BEGIN
SELECT COUNT(*) INTO quantidade FROM PRODUTOS
WHERE data_compra = CURRENT_TIMESTAMP;
END $$

DELIMITER ;
```
```
CALL Verificar_Quantidade_Produtos(@total);
SELECT @total;
```

