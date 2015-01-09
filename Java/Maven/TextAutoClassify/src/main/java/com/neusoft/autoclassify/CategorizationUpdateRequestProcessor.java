/* 
* @Author: Joshua
* @Email: liuchaozhen@neusoft.com
* @Last Modified time: 2014-09-16 11:30:53
* 
* @Description:
* This class implements Solr's UpdateRequestProcessor. It is used SimpleNaiveBayesClassifier to detect what exactly
* the new added doc's classification is. It uses IKAnalyzer to analyze new doc's specified field value.
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
*	<requestHandler name="/update" class="solr.UpdateRequestHandler">
* 		<lst name="defaults">
*       	<str name="update.chain">autoClassify</str>
*       </lst>
*   </requestHandler>
*
* @Todo:
* 1. Replace IKAnalyzer with Ansj if necessary.
*/

package com.neusoft.autoclassify;

import java.io.File;
import java.io.IOException;

import org.apache.lucene.classification.ClassificationResult;
import org.apache.lucene.classification.SimpleNaiveBayesClassifier;
import org.apache.lucene.index.AtomicReader;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.SlowCompositeReaderWrapper;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.util.BytesRef;
import org.apache.solr.common.SolrInputDocument;
import org.apache.solr.common.params.SolrParams;
import org.apache.solr.request.SolrQueryRequest;
import org.apache.solr.response.SolrQueryResponse;
import org.apache.solr.update.AddUpdateCommand;
import org.apache.solr.update.processor.UpdateRequestProcessor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.wltea.analyzer.lucene.IKAnalyzer;

class CategorizationUpdateRequestProcessor extends UpdateRequestProcessor {
	private SimpleNaiveBayesClassifier _classifier;
	private String _dbtrainField;
	private String _dbclassifyField;
	private String _trainField;
	private String _classifyField;
	protected final static Logger log = LoggerFactory.getLogger(CategorizationUpdateRequestProcessor.class);
	  
	public CategorizationUpdateRequestProcessor(SolrQueryRequest req, SolrQueryResponse rsp, UpdateRequestProcessor next) {
		super(next);
		try {
			initParams(req.getParams());
		} catch (IOException e) {
			e.printStackTrace();
			log.error("initParams error:" + e);
		}
	}
	
	/**
	 * [initParams description]
	 * @method initParams
	 * @param  params      [description]
	 * @throws IOException [description]
	 */
	private void initParams(SolrParams params) throws IOException {
		if (null != params) {
			AtomicReader atomicReader = null;
			_classifier = new SimpleNaiveBayesClassifier();

			String baseDBIndexDir = params.get("autoClassify.indexDBDir", "");
			if (null != baseDBIndexDir && baseDBIndexDir.length() > 0) {
				IndexReader reader = DirectoryReader.open(FSDirectory.open(new File(baseDBIndexDir)));
				atomicReader = SlowCompositeReaderWrapper.wrap(reader);
			}

			_trainField = params.get("autoClassify.trainField", null);
			if (null == _trainField || _trainField.length() <= 0) {
				_trainField = "content";
			}

			_classifyField = params.get("autoClassify.classifyField", null);
			if (null == _classifyField || _classifyField.length() <= 0) {
				_classifyField = "categories";
			}
			
			_dbtrainField = params.get("autoClassify.dbtrainField", null);
			if (null == _dbtrainField || _dbtrainField.length() <= 0) {
				_dbtrainField = "content";
			}

			_dbclassifyField = params.get("autoClassify.dbclassifyField", null);
			if (null == _dbclassifyField || _dbclassifyField.length() <= 0) {
				_dbclassifyField = "category";
			}

			if (null != atomicReader) {
				_classifier.train(atomicReader, _dbtrainField, _dbclassifyField, new IKAnalyzer(true));
			}
		}
	}
	
	@Override
	public void processAdd(AddUpdateCommand cmd) throws java.io.IOException {
		SolrInputDocument inputDoc = cmd.getSolrInputDocument();
		if (!inputDoc.containsKey(_classifyField) && null != _classifier) {
			ClassificationResult<BytesRef> result = _classifier.assignClass((String) inputDoc.getFieldValue(_trainField));
			String classified = result.getAssignedClass().utf8ToString();
			inputDoc.addField(_classifyField, classified);
		}

		super.processAdd(cmd);
	}
}
