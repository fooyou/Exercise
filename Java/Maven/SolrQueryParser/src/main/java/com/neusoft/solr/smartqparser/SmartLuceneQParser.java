/**
 * @Author: Joshua
 * @E-Mail: liuchaozhen@neusoft.com
 * @Date:   2014-12-12 13:25:32
 * @About SmartLuceneQParser.java
 */

package com.neusoft.solr.smartqparser;

import org.apache.lucene.search.Query;
import org.apache.solr.common.params.CommonParams;
import org.apache.solr.common.params.SolrParams;
import org.apache.solr.parser.ParseException;
import org.apache.solr.request.SolrQueryRequest;
import org.apache.solr.search.QParser;
import org.apache.solr.search.SolrQueryParser;

public class SmartLuceneQParser extends QParser {

    private SolrQueryParser _solrQueryParser;
    
    public SmartLuceneQParser(String qstr, SolrParams localParams, SolrParams params, SolrQueryRequest req) {
        super(qstr, localParams, params, req);
    }
    
    public Query parse() throws ParseException {
        String qstr = getString();
        String defaultFieldString = getParam(CommonParams.DF);
        if (null == defaultFieldString) {
            defaultFieldString = getReq().getSchema().getDefaultSearchFieldName();
        }
        
        _solrQueryParser = new SmartLuceneQParser(this, defaultFieldString)
    }
}