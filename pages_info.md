# ALIEXPRESS

## Search query:

```
https://www.aliexpress.com/w/wholesale-NOMBRE-PRODUCTO.html
```

Donde NOMBRE-PRODUCTO se remplaza por el producto a buscar.

## Search method:

```
?spm=a2g0o.productlist.TYPE.NUM
```

Donde TYPE.NUM se remplaza por:

- search: Si es una busqueda de usuario. NUM = 0.
- auto_suggest: Si es un recomenado de la barra de busqueda. NUM es el indice del sugerido en la barra de busqueda (NUM = 1 muestra el mismo resultado que search.0). El uso de NUM afecta la busqueda pues puede añadir parametros de categoria.

## Ejemplos:

```
https://www.aliexpress.com/w/wholesale-audifonos-inalambricos.html?spm=a2g0o.productlist.user.0
```

```
https://www.aliexpress.com/w/wholesale-audifonos-inalambricos.html?spm=a2g0o.productlist.auto_suggest.1
```

# TEMU

### Search query:

```
https://www.temu.com/search_result.html?search_key=NOMBRE%PRODUCTO
```

Donde NOMBRE%20PRODUCTO se remplaza por el producto a buscar.

### Search method:

```
&search_method=TYPE
```

Donde TYPE se remplaza por:

	- user: Si es una busqueda de usuario.
	- suggest; Si es un recomenado de la barra de busqueda.

### Search prefix: 

```
&sprefix=NOMBREPRODUCTO
```
Donde NOMBREPRODUCTO se remplaza por el prefijo de la busqueda (Palabra clave que representa la categoria del producto).

## Ejemplos:

```
https://www.temu.com/search_result.html?search_key=audifonos%inalambricos&search_method=user
```

```
https://www.temu.com/search_result.html?search_key=audifonos%inalambricos&search_method=suggest&sprefix=audifonos
```

