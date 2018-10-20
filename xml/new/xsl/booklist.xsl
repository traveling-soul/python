<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html xmlns="http://www.w3.org/1999/xhtml">
<meta charset="UTF-8"/>
<body>
<center>
<table border="1">
<tr>
<th>name</th>
<th>price</th>
<th>description</th>
</tr>
<xsl:for-each select="booklist/book">
<tr>
<td><xsl:value-of select="name"></xsl:value-of></td>
<td><xsl:value-of select="price"></xsl:value-of></td>
<td><xsl:value-of select="description"></xsl:value-of></td>
</tr>
</xsl:for-each>
</table>
</center>
</body>
</html>
</xsl:template>
</xsl:stylesheet>