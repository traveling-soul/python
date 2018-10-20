<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
	<html>
		<body>
			<h1>Customer Listing</h1>
			<xsl:apply-templates/>
		</body>
	</html>
</xsl:template>
<xsl:template match="customer">
	<div>
		<h3>Customer ID:
		<xsl:value-of select="@customerid"/>
		</h3>
		<xsl:apply-templates select="firstname"/>
		<xsl:apply-templates select="lastname"/>
		<xsl:apply-templates select="homephone"/>
		<xsl:apply-templates select="notes"/>
	</div>
</xsl:template>
<xsl:template match="firstname">
	<b>First Name :</b>
	<xsl:value-of select="."/>
	<br/>
</xsl:template>
<xsl:template match="laststname">
	<b>Last Name :</b>
	<xsl:value-of select="."/>
	<br/>
</xsl:template>
<xsl:template match="homephone">
	<b>Home Phone :</b>
	<xsl:value-of select="."/>
	<br/>
</xsl:template>
<xsl:template match="notes">
	<b>Notes 55t :</b>
	<xsl:value-of select="."/>
	<br/>
</xsl:template>
</xsl:stylesheet>