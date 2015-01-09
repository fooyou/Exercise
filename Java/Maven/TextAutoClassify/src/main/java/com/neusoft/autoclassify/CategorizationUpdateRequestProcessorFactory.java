/* 
* @Author: Joshua
* @Email: liuchaozhen@neusoft.com
* @Last Modified time: 2014-09-16 11:17:13
*
* @Description: 
* This class implements UpdateRequestProcessorFactory.
*  
* @How to use:
* A configuration in core conf/solrconfig.xml might like this:
*     <updateRequestProcessorChain name="autoClassify">
*       <processor class="neu.autoclassify.CategorizationUpdateRequestProcessorFactory">
*         <str name="autoClassify.indexDBDir">path/to/index/db</str>
*         <!-- <str name="autoClassify.trainField">content</str> -->
*         <!-- <str name="autoClassify.classifyField">categories</str> -->
*       </processor>
*       <processor class="solr.RunUpdateProcessorFactory" />
      </updateRequestProcessorChain>
* Also you can set default update.chain, which will automatically switch to 'update?update.chain=autoClassify':
*   <requestHandler name="/update" class="solr.UpdateRequestHandler">
*       <lst name="defaults">
*           <str name="update.chain">autoClassify</str>
*       </lst>
*   </requestHandler>
* You can see details in CategorizationUpdateRequestProcessor.java file.
*/
package com.neusoft.autoclassify;

import org.apache.solr.common.params.SolrParams;
import org.apache.solr.common.util.NamedList;
import org.apache.solr.request.SolrQueryRequest;
import org.apache.solr.response.SolrQueryResponse;
import org.apache.solr.update.processor.UpdateRequestProcessor;
import org.apache.solr.update.processor.UpdateRequestProcessorFactory;
import org.apache.solr.util.SolrPluginUtils;

public class CategorizationUpdateRequestProcessorFactory extends UpdateRequestProcessorFactory {
    protected SolrParams defaults;
    protected SolrParams appends;
    protected SolrParams invariants;

	@Override
	public UpdateRequestProcessor getInstance(SolrQueryRequest req, SolrQueryResponse rsp, UpdateRequestProcessor next) {
		// Process defaults, appends and invariants if we got a request
        if(req != null) {
            SolrPluginUtils.setDefaults(req, defaults, appends, invariants);
        }
        return new CategorizationUpdateRequestProcessor(req, rsp, next);
	}


    /**
     * The UpdateRequestProcessor may be initialized in solrconfig.xml similarly
     * to a RequestHandler, with defaults, appends and invariants.
     * @param args a NamedList with the configuration parameters 
     */
    @Override
    @SuppressWarnings("rawtypes")
    public void init( NamedList args )
    {
        if (args != null) {
            Object o;
            o = args.get("defaults");
            if (o != null && o instanceof NamedList) {
                defaults = SolrParams.toSolrParams((NamedList) o);
            } else {
                defaults = SolrParams.toSolrParams(args);
            }
            o = args.get("appends");
            if (o != null && o instanceof NamedList) {
                appends = SolrParams.toSolrParams((NamedList) o);
            }
            o = args.get("invariants");
            if (o != null && o instanceof NamedList) {
                invariants = SolrParams.toSolrParams((NamedList) o);
            }
        }
    }
}
