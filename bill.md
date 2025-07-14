# California Senate Bill 53
This document is an annotated version of SB 53

## SECTION 1.
The Legislature finds and declares all of the following:

(a) California is leading the world in artificial intelligence innovation and research through companies large and small and through the state’s remarkable public and private universities.

(b) Artificial intelligence, including new advances in foundation models, has the potential to catalyze innovation and the rapid development of a wide range of benefits for Californians and the California economy, including advances in medicine, wildfire forecasting and prevention, and climate science, and to push the bounds of human creativity and capacity.

(c) The [Joint California Policy Working Group]{This refers to a group of AI experts [convened](https://www.gov.ca.gov/2024/09/29/governor-newsom-announces-new-initiatives-to-advance-safe-and-responsible-ai-protect-californians/) by Governor Gavin Newsom in September 2024 to study how California should govern frontier AI. The Working Group was led by Stanford HAI co-director [Fei-Fei Li](https://hai.stanford.edu/people/fei-fei-li), Carnegie Endowment president [Tino Cuéllar](https://carnegieendowment.org/people/mariano-florentino-tino-cuellar?lang=en), and UC Berkeley professor [Jennifer Chayes](https://cdss.berkeley.edu/people/jennifer-chayes). They published their findings in June 2025 as the [California Report on Frontier AI Policy.](https://www.cafrontieraigov.org/)} on AI Frontier Models has recommended sound principles for policy in artificial intelligence.

(d) Targeted interventions to support effective artificial intelligence governance should balance the technology’s benefits and material risks.

(e) Artificial intelligence developers [have already voluntarily committed]{At the 2024 AI Summit in Seoul, most of America's leading AI companies voluntarily agreed to the [Frontier AI Safety Commitments](https://www.gov.uk/government/publications/frontier-ai-safety-commitments-ai-seoul-summit-2024/frontier-ai-safety-commitments-ai-seoul-summit-2024). Under these commitments each signatory must make a plan to assess and manage any severe risks their systems could pose (outcome 1), and they must disclose the results of their risk assessments to their home government (outcome 3). Google, OpenAI, Anthropic, xAI, and Meta are all signtories to the Seoul Commitments.} to creating safety and security protocols and releasing the results of risk assessments.

(f) In building a robust and transparent evidence environment, policymakers can align incentives to simultaneously protect consumers, leverage industry expertise, and recognize leading safety practices.

(g) When industry actors conduct internal research on their technologies’ impacts, a significant information asymmetry can develop between those with privileged access to data and the broader public.

(h) Greater transparency, given current information deficits, can advance accountability, competition, and public trust.

(i) Whistleblower protections and public-facing information sharing are key instruments to increase transparency.

(j) Adverse event reporting systems enable monitoring of the post-deployment impacts of artificial intelligence.

(k) There is growing evidence that, unless they are developed with careful diligence and reasonable precaution, advanced artificial intelligence systems could pose catastrophic risks from both malicious uses and malfunctions, including artificial intelligence-enabled hacking, biological attacks, and loss of control.

(l) With the frontier of artificial intelligence rapidly evolving, there is a need for legislation to track the frontier of artificial intelligence research and alert policymakers and the public to the risks and harms from the very most advanced artificial intelligence systems, while avoiding burdening smaller companies behind the frontier.

(m) A computational [threshold of 10^26 floating point operations]{According to [Epoch AI's estimates](https://epoch.ai/data/notable-ai-models), no company had ever published a foundational model above this threshold until early 2025. Since then, only two companies (OpenAI and xAI) have released models that pass the threshold.
President Biden's [Executive Order 14110](https://www.govinfo.gov/content/pkg/FR-2023-11-01/pdf/2023-24283.pdf) also used 10^26 training FLOPs as the threshold for a frontier model. Under EO 14110, any developer training a model above the threshold was required to disclose their safety testing results and security protocols to Federal authorities.} captures the current frontier of foundation model development and captures only highly resourced developers spending hundreds of millions of dollars to develop foundation models.

(n) In the future, foundation models developed by smaller companies or that are behind the frontier may pose significant catastrophic risk, and additional legislation may be needed at that time.

(o) It is the intent of the Legislature to create more transparency, but collective safety will depend in part on large developers taking due care in their development and deployment of foundation models proportional to the scale of the foreseeable risks.

## SECTION 2.
Chapter 25.1 (commencing with Section 22757.10) is added to Division 8 of the Business and Professions Code, to read:

### CHAPTER  25.1. Transparency in Frontier Artificial Intelligence Act

### 22757.10.

This chapter shall be known as the Transparency in Frontier Artificial Intelligence Act.

### 22757.11.

 For purposes of this chapter:

(a) “[Artificial intelligence model]{The definition that follows is a close paraphrase of the [OECD's definition](https://www.oecd.org/en/publications/explanatory-memorandum-on-the-updated-oecd-definition-of-an-ai-system_623da898-en.html) of an AI system, published in March 2024.}” means an engineered or machine-based system that varies in its level of autonomy and that can, for explicit or implicit objectives, infer from the input it receives how to generate outputs that can influence physical or virtual environments.

(b) “Catastrophic risk” means a foreseeable and material risk that a large developer’s development, storage, use, or deployment of a foundation model will materially contribute to the death of, or serious injury to, more than 100 people or more than one billion dollars ($1,000,000,000) in damage to rights in money or property arising from a single incident, scheme, or course of conduct involving a dangerous capability.

(c) “Critical safety incident” means any of the following:

&nbsp;&nbsp;(1) Unauthorized access to, modification of, or exfiltration of, the model weights of a foundation model.

&nbsp;&nbsp;(2) Harm resulting from the materialization of a catastrophic risk.

&nbsp;&nbsp;(3) Loss of control of a foundation model causing death, bodily injury, or damage to rights in money or property.

&nbsp;&nbsp;(4) A foundation model that uses [deceptive techniques]{Including, for instance, the alignment faking behavior displayed by Claude 3 Opus in Greenblatt et al.'s "[Alignment Faking in Large Language Models](https://assets.anthropic.com/m/983c85a201a962f/original/Alignment-Faking-in-Large-Language-Models-full-paper.pdf)" experiment.} against the large developer to subvert the controls or monitoring of its large developer outside of the context of an evaluation designed to elicit this behavior.

(d) “Dangerous capability” means the capacity of a foundation model to do any of the following:

&nbsp;&nbsp;(1) Provide expert-level assistance in the creation or release of a chemical, biological, radiological, or nuclear weapon.

&nbsp;&nbsp;(2) Conduct or assist in a cyberattack.

&nbsp;&nbsp;(3) Engage in conduct, with limited human intervention, that would, if committed by a human, constitute the crime of extortion, theft, including theft by deception, or a serious or violent felony.

&nbsp;&nbsp;(4) Evade the control of its large developer or user.

(e) (1) “Deploy” means to make a foundation model available to a third party for use, modification, copying, or combination with other software.

&nbsp;&nbsp;(2) “Deploy” does not include making a foundation model available to a third party for the primary purpose of developing or evaluating the foundation model.

(f) “Large developer” means either of the following:

&nbsp;&nbsp;(1) (A) Before January 1, 2027, “large developer” means a person who has trained, or initiated the training of, at least one foundation model using a quantity of computing power greater than 10^26 integer or floating-point operations.

&nbsp;&nbsp;&nbsp;&nbsp;(B) The quantity of computing power described in subparagraph (A) shall include computing for the original training run and any subsequent fine-tuning, reinforcement learning, or other material modifications to a preceding foundation model.

&nbsp;&nbsp;(2) (A) Except as provided in subparagraph (B), on and after January 1, 2027, “large developer” has the meaning defined by a regulation adopted by the Attorney General pursuant to Section 22757.15.

&nbsp;&nbsp;&nbsp;&nbsp;(B) If the Attorney General does not adopt a regulation described in subparagraph (A) by January 1, 2027, the definition in paragraph (1) shall be operative until the regulation is adopted.

(g) “[Foundation model]{This definition apparently counts large language models like ChatGPT but excludes narrow AI models like Google DeepMind's [AlphaFold](https://deepmind.google/science/alphafold/) or OpenAI [Five](https://openai.com/index/openai-five-defeats-dota-2-world-champions/).}” means an artificial intelligence model that is all of the following:

&nbsp;&nbsp;(1) Trained on a broad data set.

&nbsp;&nbsp;(2) Designed for generality of output.

&nbsp;&nbsp;(3) Adaptable to a wide range of distinctive tasks.

(h) “Model weight” means a numerical parameter in a foundation model that is adjusted through training and that helps determine how inputs are transformed into outputs.

(i) “Safety and security protocol” means documented technical and organizational protocols to manage, assess, and mitigate catastrophic risks.

### 22757.12.

(a) A large developer shall write, implement, and clearly and conspicuously publish on its internet website a safety and security protocol that describes in specific detail all of the following:

&nbsp;&nbsp;(1) How, if at all, the large developer excludes certain foundation models from being covered by its safety and security protocol because those foundation models do not pose material catastrophic risks.

&nbsp;&nbsp;(2) The testing procedures that the large developer uses to assess catastrophic risks from its foundation models, including risk resulting from malfunctions, misuse, and foundation models evading the control of the large developer or user.

&nbsp;&nbsp;(3) The mitigations that a large developer takes to reduce a catastrophic risk and how the large developer assesses the effectiveness of those mitigations.

&nbsp;&nbsp;(4) The degree to which the large developer’s assessments of catastrophic risk and the effectiveness of catastrophic risk mitigations are reproducible by external entities.

&nbsp;&nbsp;(5) The extent to which, and how, a large developer will use third parties to assess catastrophic risks and the effectiveness of mitigations of catastrophic risk.

&nbsp;&nbsp;(6) The large developer’s cybersecurity practices and how the large developer secures unreleased model weights from unauthorized modification or transfer by internal or external parties.

&nbsp;&nbsp;(7) To the extent that the foundation model is controlled by the large developer, the procedures the large developer will use to monitor critical safety incidents and the steps that a large developer would take to respond to a critical safety incident, including, but not limited to, who the large developer will notify and the timeline on which the large developer would take these steps.

&nbsp;&nbsp;(8) The testing procedures that the large developer will use to assess and manage a catastrophic risk resulting from the internal use of its foundation models, including risks resulting from a foundation model circumventing oversight mechanisms, and the schedule, specified in days, by which the large developer will report these assessments pursuant to subdivision (d).

&nbsp;&nbsp;(9) How the developer determines when its foundation models are substantially modified enough to conduct additional assessments and publish a transparency report pursuant to subdivision (c).

(b) If a large developer makes a material modification to its safety and security protocol, the large developer shall clearly and conspicuously publish the modified protocol and a justification for that modification within 30 days.

(c) Before or concurrently with deploying a new foundation model or a substantially modified version of an existing foundation model, a large developer shall clearly and conspicuously publish on its internet website a transparency report containing all of the following:

&nbsp;&nbsp;(1) The results of any risk assessment, the steps taken to address any identified risks, and the results of any risk mitigation assessment conducted by the large developer pursuant to its safety and security protocol.

&nbsp;&nbsp;(2) (A) The results of any risk assessment, the steps taken to address any identified risks, and the results of any risk mitigation assessment conducted pursuant to a large developer’s safety and security protocol that is conducted by a third party that contracts with a large developer.

&nbsp;&nbsp;&nbsp;&nbsp;(B) A large developer shall disclose the time and extent of predeployment access provided to any third party described in subparagraph (A), whether or not the third party was independent, and the nature of any constraints the large developer placed on the assessment or on the third party’s ability to disclose information about its assessment to the public or to government officials.

&nbsp;&nbsp;(3) (A) If the deployment would pose a catastrophic risk, the reasoning behind the large developer’s decision to deploy the foundation model, the process by which the large developer arrived at that decision, and any limitations in the assessments that the large developer used to make that decision.

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

## SECTION 3.
Section 11546.8 is added to the Government Code, to read:

### 11546.8. 

(a) There is hereby established within the Government Operations Agency a consortium that shall develop, pursuant to this section, a framework for the creation of a public cloud computing cluster to be known as “CalCompute.”

(b) The consortium shall develop a framework for the creation of CalCompute that advances the development and deployment of artificial intelligence that is safe, ethical, equitable, and sustainable by doing, at a minimum, both of the following:

(1) Fostering research and innovation that benefits the public.

(2) Enabling equitable innovation by expanding access to computational resources.

(c) The consortium shall make reasonable efforts to ensure that CalCompute is established within the University of California to the extent possible.

(d) CalCompute shall include, but not be limited to, all of the following:

(1) A fully owned and hosted cloud platform.

(2) Necessary human expertise to operate and maintain the platform.

(3) Necessary human expertise to support, train, and facilitate the use of CalCompute.

(e) The consortium shall operate in accordance with all relevant labor and workforce laws and standards.

(f) (1) On or before January 1, 2027, the Government Operations Agency shall submit, pursuant to Section 9795, a report from the consortium to the Legislature with the framework developed pursuant to subdivision (b) for the creation and operation of CalCompute.

(2) The report required by this subdivision shall include all of the following elements:

(A) A landscape analysis of California’s current public, private, and nonprofit cloud computing platform infrastructure.

(B) An analysis of the cost to the state to build and maintain CalCompute and recommendations for potential funding sources.

(C) Recommendations for the governance structure and ongoing operation of CalCompute.

(D) Recommendations for the parameters for use of CalCompute, including, but not limited to, a process for determining which users and projects will be supported by CalCompute.

(E) An analysis of the state’s technology workforce and recommendations for equitable pathways to strengthen the workforce, including the role of CalCompute.

(F) A detailed description of any proposed partnerships, contracts, or licensing agreements with nongovernmental entities, including, but not limited to, technology-based companies, that demonstrates compliance with the requirements of subdivisions (c) and (d).

(G) Recommendations regarding how the creation and ongoing management of CalCompute can prioritize the use of the current public sector workforce.

(g) The consortium shall, consistent with state constitutional law, consist of 14 members as follows:

(1) Four representatives of the University of California and other public and private academic research institutions and national laboratories appointed by the Secretary of Government Operations.

(2) Three representatives of impacted workforce labor organizations appointed by the Speaker of the Assembly.

(3) Three representatives of stakeholder groups with relevant expertise and experience, including, but not limited to, ethicists, consumer rights advocates, and other public interest advocates appointed by the Senate Rules Committee.

(4) Four experts in technology and artificial intelligence to provide technical assistance appointed by the Secretary of Government Operations.

(h) The members of the consortium shall serve without compensation, but shall be reimbursed for all necessary expenses actually incurred in the performance of their duties.

(i) The consortium shall be dissolved upon submission of the report required by paragraph (1) of subdivision (f) to the Legislature.

(j) If CalCompute is established within the University of California, the University of California may receive private donations for the purposes of implementing CalCompute.

(k) This section shall become operative only upon an appropriation in a budget act, or other measure, for the purposes of this section.

## SECTION 4.
Chapter 5.1 (commencing with Section 1107) is added to Part 3 of Division 2 of the Labor Code, to read:

### CHAPTER  5.1. Whistleblower Protections: Catastrophic Risks in AI Foundation Models

1107. For purposes of this chapter:

(a) “Artificial intelligence model” means an engineered or machine-based system that varies in its level of autonomy and that can, for explicit or implicit objectives, infer from the input it receives how to generate outputs that can influence physical or virtual environments.

(b) "Catastrophic risk" has the meaning defined in Section 22757.11 of the Business and Professions Code.

(c) “Large developer” has the meaning defined in Section 22757.11 of the Business and Professions Code.

(d) “Employee” means a person who performs services for an employer, including both of the following:

(1) A contractor, subcontractor, or an unpaid advisor involved with assessing, managing, or addressing critical catastrophic risk, including all of the following:

(A) An independent contractor.

(B) A freelance worker.

(C) A person employed by a labor contractor.

(D) A board member.

(2) Corporate officers.

(e) “Foundation model” has the same meaning as defined in Section 22757.11 of the Business and Professions Code.

(f) “Labor contractor” means an individual or entity that supplies, either with or without a contract, a client employer with workers to perform labor within the client employer’s usual course of business.

1107.1. (a) A large developer shall not make, adopt, enforce, or enter into a rule, regulation, policy, or contract that prevents an employee from disclosing, or retaliates against an employee for disclosing, information to the Attorney General, a federal authority, a person with authority over the employee, or another employee who has authority to investigate, discover, or correct the reported issue, if the employee has reasonable cause to believe that the information discloses either of the following:

(1) The large developer’s activities pose a catastrophic risk.

(2) The large developer has violated Chapter 25.1 (commencing with Section 22757.10) of Division 8 of the Business and Professions Code.

(b) A large developer shall not enter into a contract that prevents an employee from making a disclosure protected under Section 1102.5.

(c) A large developer shall not make, adopt, enforce, or enter into a rule, regulation, policy, or contract that would prevent an organization or entity that provides goods or services to the large developer related to the assessment, management, or addressing of catastrophic risk, or an employee of that organization or entity, from disclosing information to the Attorney General, a federal authority, or the developer if the organization, entity, or individual has reasonable cause to believe that the information discloses either of the following:

(1) The large developer’s activities pose a catastrophic risk.

(2) The large developer has violated Chapter 25.1 (commencing with Section 22757.10) of Division 8 of the Business and Professions Code.

(d) An employee may use the hotline described in Section 1102.7 to make reports described in subdivision (a).

(e) A large developer shall provide a clear notice to all employees of their rights and responsibilities under this section, including by doing either of the following:

(1) At all times posting and displaying within any workplace maintained by the large developer a notice to all employees of their rights under this section, ensuring that any new employee receives equivalent notice, and ensuring that any employee who works remotely periodically receives an equivalent notice.

(2) At least once each year, providing written notice to each employee of the employee’s rights under this section and ensuring that the notice is received and acknowledged by all of those employees.

(f) (1) A large developer shall provide a reasonable internal process through which an employee may anonymously disclose information to the large developer if the employee believes in good faith that the information indicates that the large developer’s activities present a catastrophic risk or that the large developer has violated Chapter 25.1 (commencing with Section 22757.10) of Division 8 of the Business and Professions Code, including a monthly update to the person who made the disclosure regarding the status of the large developer’s investigation of the disclosure and the actions taken by the large developer in response to the disclosure.

(2) (A) Except as provided in subparagraph (B), the disclosures and responses of the process required by this subdivision shall be shared with officers and directors of the large developer at least once each quarter.

(B) If an employee has alleged wrongdoing by an officer or director of the large developer in a disclosure or response, subparagraph (A) shall not apply with respect to that officer or director.

(g) The court is authorized to award reasonable attorney’s fees to a plaintiff who brings a successful action for a violation of this section.

(h) In a civil action brought pursuant to this section, once it has been demonstrated by a preponderance of the evidence that an activity proscribed by this section was a contributing factor in the alleged prohibited action against the employee, the large developer shall have the burden of proof to demonstrate by clear and convincing evidence that the alleged action would have occurred for legitimate, independent reasons even if the employee had not engaged in activities protected by this section.

(i) (1) In a civil action or administrative proceeding brought pursuant to this section, an employee may petition the superior court in any county wherein the violation in question is alleged to have occurred, or wherein the person resides or transacts business, for appropriate temporary or preliminary injunctive relief.

(2) Upon the filing of the petition for injunctive relief, the petitioner shall cause notice thereof to be served upon the person, and thereupon the court shall have jurisdiction to grant temporary injunctive relief as the court deems just and proper.

(3) In addition to any harm resulting directly from a violation of this section, the court shall consider the chilling effect on other employees asserting their rights under this section in determining whether temporary injunctive relief is just and proper.

(4) Appropriate injunctive relief shall be issued on a showing that reasonable cause exists to believe a violation has occurred.

(5) An order authorizing temporary injunctive relief shall remain in effect until an administrative or judicial determination or citation has been issued, or until the completion of a review pursuant to subdivision (b) of Section 98.74, whichever is longer, or at a certain time set by the court. Thereafter, a preliminary or permanent injunction may be issued if it is shown to be just and proper. Any temporary injunctive relief shall not prohibit a large developer from disciplining or terminating an employee for conduct that is unrelated to the claim of the retaliation.

(j) Notwithstanding Section 916 of the Code of Civil Procedure, injunctive relief granted pursuant to this section shall not be stayed pending appeal.

(k) (1) This section does not impair or limit the applicability of Section 1102.5.

(2) The remedies provided by this section are cumulative to each other and the remedies or penalties available under all other laws of this state.

## SECTION 5.

(a) The provisions of this act are severable. If any provision of this act or its application is held invalid, that invalidity shall not affect other provisions or applications that can be given effect without the invalid provision or application.

(b) This act shall be liberally construed to effectuate its purposes.

(c) The duties and obligations imposed by this act are cumulative with any other duties or obligations imposed under other law and shall not be construed to relieve any party from any duties or obligations imposed under other law and do not limit any rights or remedies under existing law.

(d) This act shall not apply to the extent that it strictly conflicts with the terms of a contract between a federal government entity and a large developer.

(e) This act shall not apply to the extent that it is preempted by federal law.