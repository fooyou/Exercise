package org.ansj.solr;

import java.io.IOException;
import java.io.InputStream;
import java.io.Reader;
import java.io.File;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.Properties;

import org.ansj.library.UserDefineLibrary;
import org.apache.lucene.analysis.Tokenizer;
import org.apache.lucene.analysis.util.ResourceLoader;
import org.apache.lucene.analysis.util.ResourceLoaderAware;
import org.apache.lucene.analysis.util.TokenizerFactory;
import org.apache.lucene.util.AttributeSource.AttributeFactory;	// For Solr 4.8
// import org.apache.lucene.util.AttributeFactory;	// For Solr 4.9
import org.nlpcn.commons.lang.tire.domain.Forest;
import org.slf4j.LoggerFactory;
import org.slf4j.Logger;

public class AnsjTokenizerFactory extends TokenizerFactory implements ResourceLoaderAware , UpdateKeeper.UpdateJob{
	private static final Logger log = LoggerFactory.getLogger(AnsjTokenizerFactory.class);
	private int analysisType = 0;
	private boolean rmPunc = true;
	private ResourceLoader loader; 
	
	private long lastUpdateTime = -1;
	private String conf = null;
	
	
	public AnsjTokenizerFactory(Map<String, String> args) {
		super(args);
		assureMatchVersion();
		analysisType = getInt(args, "analysisType", 0);
		rmPunc = getBoolean(args, "rmPunc", true);
		conf = get(args, "conf");
		log.info(":::ansj:construction::::::::::::::::::::::::::" + conf);
	}

	public void update() {
		Properties p = canUpdate();
		if (p != null){
			List<String> dicPaths = SplitFileNames(p.getProperty("files"));
			for (String path : dicPaths) {
				if ((path != null && !path.isEmpty())) {
					
					Forest forest = new Forest();
					File dic = new File(path);
					if (!dic.canRead() || dic.isHidden()) {
						log.warn("init userLibrary  warning :" + new File(path).getAbsolutePath() + " because : file not found or failed to read !");
						return;
					}
					UserDefineLibrary.loadLibrary(forest, path);

					// 将新构建的辞典树替换掉舊的。
					UserDefineLibrary.FOREST = forest;
				}
			}
		}
	}

	public void inform(ResourceLoader loader) throws IOException {
		log.info(":::ansj:::inform::::::::::::::::::::::::" + conf);
		this.loader = loader;
		this.update();
		if(conf != null && !conf.trim().isEmpty()){
			UpdateKeeper.getInstance().register(this);
		}
	}

	@Override
	public Tokenizer create(AttributeFactory factory, Reader input) {
		return new AnsjTokenizer(input, analysisType, rmPunc);
	}
	
	public static List<String> SplitFileNames(String fileNames) {
		if (fileNames == null)
			return Collections.<String> emptyList();
		List<String> result = new ArrayList<String>();
		for (String file : fileNames.split("[,\\s]+")) {
			result.add(file);
		}
		return result;
	}
	
	private Properties canUpdate() {

		try{
			if (conf == null)
				return null;
			Properties p = new Properties();
			InputStream confStream = loader.openResource(conf);
			p.load(confStream);
			confStream.close();
			String lastupdate = p.getProperty("lastupdate", "0");
			Long t = new Long(lastupdate);
			
			if (t > this.lastUpdateTime){
				this.lastUpdateTime = t.longValue();
				String paths = p.getProperty("files");
				if (paths==null || paths.trim().isEmpty()) 
					return null;
				System.out.println("loading conf");
				return p;
			}else{
				this.lastUpdateTime = t.longValue();
				return null;
			}
		}catch(Exception e){
			log.error("ansj parsing conf NullPointerException~~~~~" + e.getMessage());
			return null;
		}
	}
	
}
