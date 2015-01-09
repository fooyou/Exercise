/**
 * @Author: Joshua
 * @E-Mail: liuchaozhen@neusoft.com
 * @Date:   2014-12-12 21:15:40
 * @About SmartSolrQParser.java
 */

package com.neusoft.solr.smartqparser;

import org.apache.solr.search.QParser;
import org.apache.solr.search.SolrQueryParser;

public class SmartSolrQParser extends SolrQueryParser {
    public SmartSolrQParser(QParser schema, String defaultField) {
        super(schema, defaultField);
    }
    
}