# Test Backend

## Consideraciones

- El proyecto está incompleto, por lo cual si encuentras algun error de configuración o algo que te impida avanzar, corrígelo
- Los Tests pueden estar mal escritos o no hacer sentido, si necesitas puedes modificarlos
- Es ideal que no utilices la ORM dentro de las vistas y el acceso a datos sea a través de la capa de servicios


## Tests

Para ejecutar los tests se sugiere el siguiente comando `docker-compose run --rm django pytest`

## TODO

- Eliminar todos los skips de los tests y lograr que estos pasen correctamente
- Crear un CRUD para el modelo `Product`, deberás crear todos los endpoints y sus tests correspondientes.
