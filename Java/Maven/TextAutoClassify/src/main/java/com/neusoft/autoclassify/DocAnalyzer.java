/* 
* @Author: joshua
* @Email: liuchaozhen@neusoft.com
* @Date:   2014-09-25 14:02:28
* @Last Modified by:   joshua
* @Last Modified time: 2014-09-25 14:28:52
*
* @Description: 
* 
* @Todo: 
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
import org.wltea.analyzer.lucene.IKAnalyzer;

public class DocAnalyzer {
	private SimpleNaiveBayesClassifier _classifier = null;
	private String _dbDir;
	private String _dbTrainField;
	private String _dbClassifyField;
	
	/**
	 * Constructor.
	 * @param  indexDBDir: The path to trained lucene index db.
	 * @param  dbTrainField: The field name of trained content.
	 * @param  dbClassifyField: Specify the category field name.
	 */
	public DocAnalyzer(String indexDBDir, String dbTrainField, String dbClassifyField) {
		_dbDir = indexDBDir;
		_dbTrainField = dbTrainField;
		_dbClassifyField = dbClassifyField;
	}
	
	private void InitParam() throws IOException {
		_classifier = new SimpleNaiveBayesClassifier();
		AtomicReader atomicReader = null;
		
		if (null != _dbDir && _dbDir.length() > 0) {
			IndexReader reader = DirectoryReader.open(FSDirectory.open(new File(_dbDir)));
			atomicReader = SlowCompositeReaderWrapper.wrap(reader);
		} else {
			throw new NullPointerException("Index DB Dir in null.");
		}
		
		if (null != atomicReader) {
			_classifier.train(atomicReader, _dbTrainField, _dbClassifyField, new IKAnalyzer(true));
		} else {
			throw new NullPointerException("Error read index db.");
		}
	}
	
	/**
	 * [Analyze description]
	 * @method Analyze
	 * @param  content: The content to be analyzed.
	 * @return Category name in String type.
	 * @throws IOException [description]
	 */
	public String Analyze(String content) throws IOException {
		String category = "";
		if (null == _classifier) {
			InitParam();
		}
		
		if (null != content && content.length() > 0) {
			ClassificationResult<BytesRef> result = _classifier.assignClass(content);
			category = result.getAssignedClass().utf8ToString();
		}
		return category;
	}
}
