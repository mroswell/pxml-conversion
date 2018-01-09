<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:p="http://www.palantirtech.com/pg/schema/import/">
    <xsl:output method="text" />
    <xsl:template match="/p:palantir">
        <xsl:for-each select="./p:graph/p:objectSet/p:object">
            <xsl:value-of select="'&quot;'"/>
            <xsl:value-of select="p:noteSet/p:note/p:noteData/text()"/>
            <xsl:value-of select="'&quot;,&quot;'"/>
            <xsl:value-of select="p:propertySet/p:property/p:propertyValue/p:propertyData/text()"/>
            <xsl:value-of select="'&quot;'"/>
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>
