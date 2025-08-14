import jenkins.model.*;
import org.jenkinsci.plugins.workflow.libs.*;
import jenkins.scm.api.SCMSource;

SCMSource scm = new jenkins.plugins.git.GitSCMSource("https://github.com/manupanand-freelance-developer/ci-jenkins-prjt-infra-11-2025.git")
scm.setCredentialsId("")

LibraryRetriever libRetriever = new SCMSourceRetriever(scm)

LibraryConfiguration libConfig = new LibraryConfiguration("shared-pipeline",libRetriever)
libConfig.setDefaultVersion("main")
libConfig.setImplicit(false)
libConfig.setIncludeInChangesets(true)

List<LibraryConfiguration> libraries =  new ArrayList<LibraryConfiguration>()
libraries.add(libConfig)

GlobalLibraries globalLibs = GlobalConfiguration.all().get(GlobalLibraries.class)
globalLibs.setLibraries(libraries)
 