# California Senate Bill 53
This document is an annotated version of SB 53

## _SECTION 1._
The Legislature finds and declares all of the following:

(a) California is leading the world in artificial intelligence innovation and research through companies large and small and through the state’s remarkable public and private universities.

(b) Artificial intelligence, including new advances in foundation models, has the potential to catalyze innovation and the rapid development of a wide range of benefits for Californians and the California economy, including advances in medicine, wildfire forecasting and prevention, and climate science, and to push the bounds of human creativity and capacity.

(c) The Joint California Policy Working Group on AI Frontier Models has recommended sound principles for policy in artificial intelligence.

(d) Targeted interventions to support effective artificial intelligence governance should balance the technology’s benefits and material risks.

(e) Artificial intelligence developers have already voluntarily committed to creating safety and security protocols and releasing the results of risk assessments.

(f) In building a robust and transparent evidence environment, policymakers can align incentives to simultaneously protect consumers, leverage industry expertise, and recognize leading safety practices.

(g) When industry actors conduct internal research on their technologies’ impacts, a significant information asymmetry can develop between those with privileged access to data and the broader public.

(h) Greater transparency, given current information deficits, can advance accountability, competition, and public trust.

(i) Whistleblower protections and public-facing information sharing are key instruments to increase transparency.

(j) Adverse event reporting systems enable monitoring of the post-deployment impacts of artificial intelligence.

(k) There is growing evidence that, unless they are developed with careful diligence and reasonable precaution, advanced artificial intelligence systems could pose catastrophic risks from both malicious uses and malfunctions, including artificial intelligence-enabled hacking, biological attacks, and loss of control.

(l) With the frontier of artificial intelligence rapidly evolving, there is a need for legislation to track the frontier of artificial intelligence research and alert policymakers and the public to the risks and harms from the very most advanced artificial intelligence systems, while avoiding burdening smaller companies behind the frontier.

(m) A computational threshold of 10^26 floating point operations captures the current frontier of foundation model development and captures only highly resourced developers spending hundreds of millions of dollars to develop foundation models.

(n) In the future, foundation models developed by smaller companies or that are behind the frontier may pose significant catastrophic risk, and additional legislation may be needed at that time.

(o) It is the intent of the Legislature to create more transparency, but collective safety will depend in part on large developers taking due care in their development and deployment of foundation models proportional to the scale of the foreseeable risks.

## _SEC. 2._
 Chapter 25.1 (commencing with Section 22757.10) is added to Division 8 of the Business and Professions Code, to read:

### CHAPTER  25.1. Transparency in Frontier Artificial Intelligence Act

### 22757.10.

This chapter shall be known as the Transparency in Frontier Artificial Intelligence Act.

### 22757.11.

 For purposes of this chapter:

(a) “[Artificial intelligence model]{The definition that follows is a close paraphrase of the [OECD's definition](https://www.oecd.org/en/publications/explanatory-memorandum-on-the-updated-oecd-definition-of-an-ai-system_623da898-en.html) of an AI system, published in March 2024.}” means an engineered or machine-based system that varies in its level of autonomy and that can, for explicit or implicit objectives, infer from the input it receives how to generate outputs that can influence physical or virtual environments.

(b) “Catastrophic risk” means a foreseeable and material risk that a large developer’s development, storage, use, or deployment of a foundation model will materially contribute to the death of, or serious injury to, more than 100 people or more than one billion dollars ($1,000,000,000) in damage to rights in money or property arising from a single incident, scheme, or course of conduct involving a dangerous capability.

(c) “Critical safety incident” means any of the following:

(1) Unauthorized access to, modification of, or exfiltration of, the model weights of a foundation model.

(2) Harm resulting from the materialization of a catastrophic risk.

(3) Loss of control of a foundation model causing death, bodily injury, or damage to rights in money or property.

(4) A foundation model that uses deceptive techniques against the large developer to subvert the controls or monitoring of its large developer outside of the context of an evaluation designed to elicit this behavior.

(d) “Dangerous capability” means the capacity of a foundation model to do any of the following:

(1) Provide expert-level assistance in the creation or release of a chemical, biological, radiological, or nuclear weapon.

(2) Conduct or assist in a cyberattack.

(3) Engage in conduct, with limited human intervention, that would, if committed by a human, constitute the crime of extortion, theft, including theft by deception, or a serious or violent felony.

(4) Evade the control of its large developer or user.

(e) (1) “Deploy” means to make a foundation model available to a third party for use, modification, copying, or combination with other software.

(2) “Deploy” does not include making a foundation model available to a third party for the primary purpose of developing or evaluating the foundation model.

(f) “Large developer” means either of the following:

(1) (A) Before January 1, 2027, “large developer” means a person who has trained, or initiated the training of, at least one foundation model using a quantity of computing power greater than 10^26 integer or floating-point operations.

(B) The quantity of computing power described in subparagraph (A) shall include computing for the original training run and any subsequent fine-tuning, reinforcement learning, or other material modifications to a preceding foundation model.

(2) (A) Except as provided in subparagraph (B), on and after January 1, 2027, “large developer” has the meaning defined by a regulation adopted by the Attorney General pursuant to Section 22757.15.

(B) If the Attorney General does not adopt a regulation described in subparagraph (A) by January 1, 2027, the definition in paragraph (1) shall be operative until the regulation is adopted.

(g) “Foundation model” means an artificial intelligence model that is all of the following:

(1) Trained on a broad data set.

(2) Designed for generality of output.

(3) Adaptable to a wide range of distinctive tasks.

(h) “Model weight” means a numerical parameter in a foundation model that is adjusted through training and that helps determine how inputs are transformed into outputs.

(i) “Safety and security protocol” means documented technical and organizational protocols to manage, assess, and mitigate catastrophic risks.

### 22757.12.

 (a) A large developer shall write, implement, and clearly and conspicuously publish on its internet website a safety and security protocol that describes in specific detail all of the following:

(1) How, if at all, the large developer excludes certain foundation models from being covered by its safety and security protocol because those foundation models do not pose material catastrophic risks.

(2) The testing procedures that the large developer uses to assess catastrophic risks from its foundation models, including risk resulting from malfunctions, misuse, and foundation models evading the control of the large developer or user.

(3) The mitigations that a large developer takes to reduce a catastrophic risk and how the large developer assesses the effectiveness of those mitigations.

(4) The degree to which the large developer’s assessments of catastrophic risk and the effectiveness of catastrophic risk mitigations are reproducible by external entities.

(5) The extent to which, and how, a large developer will use third parties to assess catastrophic risks and the effectiveness of mitigations of catastrophic risk.

(6) The large developer’s cybersecurity practices and how the large developer secures unreleased model weights from unauthorized modification or transfer by internal or external parties.

(7) To the extent that the foundation model is controlled by the large developer, the procedures the large developer will use to monitor critical safety incidents and the steps that a large developer would take to respond to a critical safety incident, including, but not limited to, who the large developer will notify and the timeline on which the large developer would take these steps.

(8) The testing procedures that the large developer will use to assess and manage a catastrophic risk resulting from the internal use of its foundation models, including risks resulting from a foundation model circumventing oversight mechanisms, and the schedule, specified in days, by which the large developer will report these assessments pursuant to subdivision (d).

(9) How the developer determines when its foundation models are substantially modified enough to conduct additional assessments and publish a transparency report pursuant to subdivision (c).

(b) If a large developer makes a material modification to its safety and security protocol, the large developer shall clearly and conspicuously publish the modified protocol and a justification for that modification within 30 days.

(c) Before or concurrently with deploying a new foundation model or a substantially modified version of an existing foundation model, a large developer shall clearly and conspicuously publish on its internet website a transparency report containing all of the following:

(1) The results of any risk assessment, the steps taken to address any identified risks, and the results of any risk mitigation assessment conducted by the large developer pursuant to its safety and security protocol.

(2) (A) The results of any risk assessment, the steps taken to address any identified risks, and the results of any risk mitigation assessment conducted pursuant to a large developer’s safety and security protocol that is conducted by a third party that contracts with a large developer.

(B) A large developer shall disclose the time and extent of predeployment access provided to any third party described in subparagraph (A), whether or not the third party was independent, and the nature of any constraints the large developer placed on the assessment or on the third party’s ability to disclose information about its assessment to the public or to government officials.

(3) (A) If the deployment would pose a catastrophic risk, the reasoning behind the large developer’s decision to deploy the foundation model, the process by which the large developer arrived at that decision, and any limitations in the assessments that the large developer used to make that decision.

(B) A large developer may reuse an answer previously provided under subparagraph (A) if the rationale in question has not materially changed for the new deployment.

(d) A large developer shall clearly and conspicuously publish on its internet website any assessment of catastrophic risk resulting from internal use of its foundation models pursuant to the schedule the developer specifies in its safety and security protocol.

(e) A large developer shall not make a materially false or misleading statement about catastrophic risk from its foundation models or its management of catastrophic risk.

(f) (1) When a large developer publishes documents to comply with this section, the large developer may make redactions to those documents that are necessary to protect the large developer’s trade secrets, the large developer’s cybersecurity, public safety, or the national security of the United States or to comply with any federal or state law.

(2) If a large developer redacts information in a document pursuant to this subdivision, the large developer shall describe the character and justification of the redaction in any published version of the document to the extent permitted by the concerns that justify redaction and shall retain the unredacted information for five years.

### 22757.13.

 (a) The Attorney General shall establish a mechanism to be used by a large developer or a member of the public to report a critical safety incident that includes all of the following:

(1) The date of the critical safety incident.

(2) The reasons the incident qualifies as a critical safety incident.

(3) A short and plain statement describing the critical safety incident.

(b) A large developer shall report any critical safety incident pertaining to one or more of its foundation models to the Attorney General within 15 days of discovering the critical safety incident.

(c) The Attorney General shall review critical safety incident reports submitted by large developers and may review reports submitted by members of the public.

### 22757.14.

 (a) A violation of this chapter shall be subject to a civil penalty in an amount not to exceed  dollars ($) per violation, unless the violation is willful or reckless, in which case the civil penalty shall be in an amount not to exceed  dollars ($).

(b) The civil penalty shall be assessed in a civil action brought only by the Attorney General.

### 22757.15.

 (a) On or before January 1, 2027, and annually thereafter, the Attorney General may adopt regulations to update the definition of a “large developer” for the purposes of this chapter to ensure that it accurately reflects technological developments, scientific literature, and widely accepted national and international standards and applies to well-resourced large developers at the frontier of artificial intelligence development.

(b) In developing regulations pursuant to this section, the Attorney General shall take into account all of the following:

(1) Similar thresholds used in international standards or federal law, guidance, or regulations for the management of catastrophic risk.

(2) Input from stakeholders, including academics, industry, the open-source community, and governmental entities.

(3) The extent to which a person will be able to determine, before beginning to train or deploy a foundation model, whether that person will be subject to the regulations as a large developer with an aim toward allowing earlier determinations if possible.

(4) The complexity of determining whether a person is covered, with an aim toward allowing simpler determinations if possible.

(5) The external verifiability of determining whether a person is covered, with an aim toward definitions that are verifiable by parties other than the large developer.

(c) If the Attorney General determines that less well-resourced developers, or developers significantly behind the frontier of artificial intelligence, may create substantial catastrophic risk, the Attorney General shall promptly submit a report to the Legislature, pursuant to Section 9795, with a proposal for managing this source of catastrophic risk but shall not include those developers within the definition of “large developer” without authorization in subsequently enacted legislation.