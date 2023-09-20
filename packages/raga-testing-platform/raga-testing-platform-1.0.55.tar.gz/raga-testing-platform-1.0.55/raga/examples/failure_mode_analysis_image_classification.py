from raga import *
import datetime
from raga._tests import failure_mode_analysis, clustering

run_name = f"loader_failure_mode_analysis_image_classification-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"

test_session = TestSession(project_name="LivenessDetection", run_name= run_name, access_key="u4amNsYmYE0hQWCPPFQ8", secret_key="FUDZ3NxORAqyCCmY7eezJEU9gxX0uPM232V1g75W", host="http://13.126.220.245:8080")

rules = FMARules()
rules.add(metric="Precision", conf_threshold=0.5, metric_threshold=0.5, label="live")
rules.add(metric="Recall", conf_threshold=0.5, metric_threshold=0.5, label="live")
rules.add(metric="F1Score", conf_threshold=0.5, metric_threshold=0.5, label="live")

cls_default = clustering(method="k-means", embedding_col="ImageVectorsM1", level="image", args= {"numOfClusters": 9})

edge_case_detection = failure_mode_analysis(test_session=test_session,
                                            dataset_name = "live-dataset",
                                            test_name = "Test",
                                            model = "modelB",
                                            gt = "GT",
                                            rules = rules,
                                            type="embeddings",
                                            output_type="multi-label",
                                            clustering = cls_default)

test_session.add(edge_case_detection)

test_session.run()