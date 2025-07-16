# California Senate Bill 53
This site presents the text of Senate Bill 53 enriched with background and commentary. Click on any of the blue highlights to learn more. The bill text presented below was last amended on 8 July, 2025.

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

(j) [Adverse event reporting systems]{Much like the FDA's [Adverse Event Reporting System](https://www.fda.gov/drugs/surveillance/fdas-adverse-event-reporting-system-faers), a database that records adverse symptoms suffered by patients on FDA-approved drugs. FAERS exists to help drug regulators identify rare or long-latency effects of drugs that might not have been detected in pre-market clinical trials.\\
Similarly, adverse event reporting systems for AI could help AI regulators identify undesirable properties of models that might not have been caught in pre-deployment safety testing.} enable monitoring of the post-deployment impacts of artificial intelligence.

(k) There is growing evidence that, unless they are developed with careful diligence and reasonable precaution, advanced artificial intelligence systems could pose catastrophic risks from both malicious uses and malfunctions, including artificial intelligence-enabled hacking, biological attacks, and loss of control.

(l) With the frontier of artificial intelligence rapidly evolving, there is a need for legislation to track the frontier of artificial intelligence research and alert policymakers and the public to the risks and harms from the very most advanced artificial intelligence systems, while avoiding burdening smaller companies behind the frontier.

(m) A computational [threshold of 10^26 floating point operations]{According to [Epoch AI's estimates](https://epoch.ai/data/notable-ai-models), no company had ever published a foundational model above this threshold until early 2025. Since then, only two companies (OpenAI and xAI) have released models that pass the threshold.\\
President Biden's [Executive Order 14110](https://www.govinfo.gov/content/pkg/FR-2023-11-01/pdf/2023-24283.pdf) also used 10^26 training FLOPs as the threshold for a frontier model. Under EO 14110, any developer training a model above the threshold was required to disclose their safety testing results and security protocols to Federal authorities.} captures the current frontier of foundation model development and captures only highly resourced developers spending hundreds of millions of dollars to develop foundation models.

(n) In the future, foundation models developed by [smaller companies or that are behind the frontier]{The main reason why companies behind the frontier could eventually pose catastrophic risk is algorithmic progress. Every year, machine learning researchers discover new ways to make their learning algorithms more efficient, allowing them to train a model with a given level of performance using fewer FLOPS than previously would have been needed. Epoch AI have estimated the rate of algorithmic progress for language models, and [they find](https://epoch.ai/blog/algorithmic-progress-in-language-models) that from 2012 to 2023, the FLOPS required to achieve some fixed level of performance halved every eight months. If this trend holds, a model that takes 10^26 FLOPs to train now will take two orders of magnitude fewer FLOPs in five years.} may pose significant catastrophic risk, and additional legislation may be needed at that time.

(o) It is the intent of the Legislature to create more transparency, but collective safety will depend in part on large developers taking due care in their development and deployment of foundation models proportional to the scale of the foreseeable risks.

## SECTION 2.
Chapter 25.1 (commencing with Section 22757.10) is added to Division 8 of the Business and Professions Code, to read:

### CHAPTER  25.1. Transparency in Frontier Artificial Intelligence Act

### 22757.10.

This chapter shall be known as the Transparency in Frontier Artificial Intelligence Act.

### 22757.11.

 For purposes of this chapter:

(a) “[Artificial intelligence model]{This definition is a close paraphrase of the [OECD's definition](https://www.oecd.org/en/publications/explanatory-memorandum-on-the-updated-oecd-definition-of-an-ai-system_623da898-en.html) of an AI system, published in March 2024.}” means an engineered or machine-based system that varies in its level of autonomy and that can, for explicit or implicit objectives, infer from the input it receives how to generate outputs that can influence physical or virtual environments.

(b) “Catastrophic risk” means a foreseeable and material risk that a large developer’s development, storage, use, or deployment of a foundation model will materially contribute to the death of, or serious injury to, more than [100 people]{TODO, summarize threat models.} or more than [one billion dollars]{TODO, summarize threat models} ($1,000,000,000) in damage to rights in money or property arising from a single incident, scheme, or course of conduct involving a dangerous capability.

(c) “Critical safety incident” means any of the following:

&nbsp;&nbsp;(1) Unauthorized access to, modification of, or exfiltration of, the model weights of a foundation model.

&nbsp;&nbsp;(2) Harm resulting from the materialization of a catastrophic risk.

&nbsp;&nbsp;(3) Loss of control of a foundation model causing death, bodily injury, or damage to rights in money or property.

&nbsp;&nbsp;(4) A foundation model that uses [deceptive techniques]{For instance, a model could hide its true desires and motivations from its developers in hopes of protecting those desires from modification. [Greenblatt et al.](https://www.anthropic.com/research/alignment-faking) observed this behavior in Claude 3 Opus in their "Alignment Faking in Large Language Models" experiment.\\
A model might also intentionally underperform on capabilities tests, either because it was deliberately trained to do so by its developers, or because the model wants to hide its full capabilities from its own developers. This behavior is usually called "sandbagging," and [van der Weij et al.](https://arxiv.org/abs/2406.07358v2) have demonstrated that frontier models were already capable of sophisticated sandbagging in mid-2024.} against the large developer to subvert the controls or monitoring of its large developer outside of the context of an evaluation designed to elicit this behavior.

(d) “[Dangerous capability]{This definition of dangerous capabilities aligns with definitions found in the scientific literature. See, for instance, foundational papers by [Phuong et al.](https://deepmind.google/research/publications/78150/) and [Shevlane et al.](https://www.governance.ai/research-paper/model-evaluation-for-extreme-risks)\\
The ability to persuade or manipulate humans is also sometimes considered a dangerous model capability. Capabilities (3) and (4) below could implicitly include dangerous persuasion.}” means the capacity of a foundation model to do any of the following:

&nbsp;&nbsp;(1) Provide expert-level assistance in the creation or release of a chemical, biological, radiological, or nuclear weapon.

&nbsp;&nbsp;(2) Conduct or assist in a cyberattack.

&nbsp;&nbsp;(3) Engage in conduct, with limited human intervention, that would, if committed by a human, constitute the crime of extortion, theft, including theft by deception, or a serious or violent felony.

&nbsp;&nbsp;(4) Evade the control of its large developer or user.

(e) (1) “[Deploy]{This definition counts both closed source releases—where users are allowed to query a model only through a web app or API—and open source releases—where users are given full access to a model's weights—as deployments.}” means to make a foundation model available to a third party for use, modification, copying, or combination with other software.

&nbsp;&nbsp;(2) “Deploy” does not include making a foundation model available to a third party for the primary purpose of developing or evaluating the foundation model.

(f) “Large developer” means either of the following:

&nbsp;&nbsp;(1) (A) Before January 1, 2027, “large developer” means a person who has trained, or initiated the training of, at least one foundation model using a quantity of computing power greater than 10^26 integer or floating-point operations.

&nbsp;&nbsp;&nbsp;&nbsp;(B) The quantity of computing power described in subparagraph (A) shall include computing for the original training run and any [subsequent fine-tuning, reinforcement learning, or other material modifications]{Fine-tuning and RL are often referred to as "post-training", a catch-all for the adjustments AI companies make to a model after an initial pre-training run. Post-training already consumes a significant share of a frontier training run's compute budget. [xAI claims](https://www.interconnects.ai/p/grok-4-an-o3-look-alike-in-search) that more than half of the FLOPs used to train Grok 4 were spent on RL. If this is true, Grok 4's post-training compute already surpasses the 10^26 FLOP threshold, even without counting pre-training compute.\\
It's expected that future frontier runs will allocate an even larger share of their compute to post-training, as AI companies continue [teaching their models to reason](https://benjamintodd.substack.com/p/teaching-ai-to-reason-this-years) through chain of thought RL.} to a preceding foundation model.

&nbsp;&nbsp;(2) (A) Except as provided in subparagraph (B), on and after January 1, 2027, “large developer” has the meaning defined by a regulation adopted by the Attorney General pursuant to Section 22757.15.

&nbsp;&nbsp;&nbsp;&nbsp;(B) If the Attorney General does not adopt a regulation described in subparagraph (A) by January 1, 2027, the definition in paragraph (1) shall be operative until the regulation is adopted.

(g) “[Foundation model]{This definition apparently counts large language models like ChatGPT but excludes narrow AI models like Google DeepMind's [AlphaFold](https://deepmind.google/science/alphafold/) or OpenAI [Five](https://openai.com/index/openai-five-defeats-dota-2-world-champions/).}” means an artificial intelligence model that is all of the following:

&nbsp;&nbsp;(1) Trained on a broad data set.

&nbsp;&nbsp;(2) Designed for generality of output.

&nbsp;&nbsp;(3) Adaptable to a wide range of distinctive tasks.

(h) “[Model weight]{TODO, elaborate for the unfamiliar.}” means a numerical parameter in a foundation model that is adjusted through training and that helps determine how inputs are transformed into outputs.

(i) “Safety and security protocol” means documented technical and organizational protocols to manage, assess, and mitigate catastrophic risks.

### 22757.12.

(a) A large developer shall write, implement, and clearly and conspicuously publish on its internet website a [safety and security protocol]{TODO, summarize existing frontier safety policies.} that describes in specific detail all of the following:

&nbsp;&nbsp;(1) How, if at all, the large developer excludes certain foundation models from being covered by its safety and security protocol because those foundation models do not pose material catastrophic risks.

&nbsp;&nbsp;(2) The [testing procedures]{TODO: Who is in compliance?} that the large developer uses to assess catastrophic risks from its foundation models, including risk resulting from malfunctions, misuse, and foundation models evading the control of the large developer or user.

&nbsp;&nbsp;(3) The mitigations that a large developer takes to reduce a catastrophic risk and how the large developer assesses the effectiveness of those mitigations.

&nbsp;&nbsp;(4) The degree to which the large developer’s assessments of catastrophic risk and the effectiveness of catastrophic risk mitigations are reproducible by external entities.

&nbsp;&nbsp;(5) The extent to which, and how, a large developer will [use third parties to assess]{TODO: Who is in compliance?} catastrophic risks and the effectiveness of mitigations of catastrophic risk.

&nbsp;&nbsp;(6) The large developer’s [cybersecurity practices]{TODO: Who is in compliance?} and how the large developer secures unreleased model weights from unauthorized modification or transfer by internal or external parties.

&nbsp;&nbsp;(7) To the extent that the foundation model is controlled by the large developer, the procedures the large developer will use to monitor critical safety incidents and the steps that a large developer would take to respond to a critical safety incident, including, but not limited to, who the large developer will notify and the timeline on which the large developer would take these steps.

&nbsp;&nbsp;(8) The testing procedures that the large developer will use to assess and manage a [catastrophic risk resulting from the internal use]{That is, catastrophic risk resulting from a large developer using a model that has not yet been publicly deployed. Even before deployment, a model is vulnerable to theft by malicious outside actors and to catastrophic misuse by the developer's own staff. More speculatively, if a developer used a powerful misaligned model internally on sensitive engineering tasks, the model might strategically sabotage those tasks, causing a catastrophe at some later point. A misaligned model might also attempt to exfiltrate its own weights from the developer's computers before it is intentionally deployed. (Scientists have [already observed](https://www.anthropic.com/research/alignment-faking) models attempting to self-exfiltrate in controlled evaluations.)\\
For more analysis of risks from internal use of AI models, see "[AI models can be dangerous before public deployment](https://metr.org/blog/2025-01-17-ai-models-dangerous-before-public-deployment/)" by METR and "[AI Behind Closed Doors](https://www.apolloresearch.ai/research/ai-behind-closed-doors-a-primer-on-the-governance-of-internal-deployment)" by Apollo Research.} of its foundation models, including risks resulting from a foundation model circumventing oversight mechanisms, and the schedule, specified in days, by which the large developer will report these assessments pursuant to subdivision (d).

&nbsp;&nbsp;(9) How the developer determines when its foundation models are substantially [modified enough to conduct additional assessments]{AI developers will often make modifications to an AI system after its initial public deployment. For example, they might revise the [system prompt](https://docs.anthropic.com/en/release-notes/system-prompts), give the base model access to [additional tools](https://openai.com/index/introducing-chatgpt-search/), or raise the amount of compute the model is allowed to spend on [inference](https://www.nvidia.com/en-us/glossary/ai-inference/). All of these post-deployment updates can increase the model's dangerous capabilities or give it new dangerous propensities, potentially invalidating previous safety assessments.} and publish a transparency report pursuant to subdivision (c).

(b) If a large developer makes a material modification to its safety and security protocol, the large developer shall clearly and conspicuously publish the modified protocol and a justification for that modification within 30 days.

(c) Before or concurrently with deploying a new foundation model or a substantially [modified version of an existing foundation model]{Subparagraph (a9) above leaves it up to developers to determine when an update to an existing model is substantial enough to require a new transparency report.\\ 
Measure 7.6 in the EU AI Act's [Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) requires a large AI developer to update a model report after deployment whenever they "have reasonable grounds to believe that the justification for why the systemic risks stemming from the model are acceptable…has been materially undermined." This requirement could be triggered when a major post-deployment update is made to a model, when the model's "use and/or integrations" change materially, or when a serious incident "involving the model or a similar model" occurs. In general, the EU Code of Practice requires more active updates to transparency reports than SB 53 would require.\\
OpenAI has already [announced its intention](https://openai.com/global-affairs/eu-code-of-practice/) to sign the AI Act Code of Practice voluntarily.}, a large developer shall clearly and conspicuously publish on its internet website a [transparency report]{TODO, compare with model cards} containing all of the following:

&nbsp;&nbsp;(1) The results of any risk assessment, the steps taken to address any identified risks, and the results of any risk mitigation assessment conducted by the large developer pursuant to its safety and security protocol.

&nbsp;&nbsp;(2) (A) The results of any risk assessment, the steps taken to address any identified risks, and the results of any risk mitigation assessment conducted pursuant to a large developer’s safety and security protocol that is conducted by a third party that contracts with a large developer.

&nbsp;&nbsp;&nbsp;&nbsp;(B) A large developer shall disclose the time and extent of predeployment access provided to any third party described in subparagraph (A), whether or not the third party was independent, and the nature of any constraints the large developer placed on the assessment or on the third party’s ability to disclose information about its assessment to the public or to government officials.

&nbsp;&nbsp;(3) (A) If the deployment would pose a catastrophic risk, the reasoning behind the large developer’s decision to deploy the foundation model, the process by which the large developer arrived at that decision, and any limitations in the assessments that the large developer used to make that decision.

&nbsp;&nbsp;&nbsp;&nbsp;(B) A large developer may reuse an answer previously provided under subparagraph (A) if the rationale in question has not materially changed for the new deployment.

(d) A large developer shall clearly and conspicuously publish on its internet website any assessment of catastrophic risk resulting from internal use of its foundation models pursuant to the schedule the developer specifies in its safety and security protocol.

(e) A large developer shall not make a [materially false or misleading statement]{Some false or misleading statements about catastrophic risk management might already be penalized under existing law.\\
California's [Unfair Competition Law](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?division=7.&chapter=5.&part=2.&lawCode=BPC) already forbids businesses from making "unfair, deceptive, untrue or misleading" claims about their products to consumers. If a large developer makes false or misleading statements to its users about catastrophic risks, it could thus expose itself to civil penalties under UCL. But UCL also has limitations. The fine for making a false or misleading statement is capped at $2,500, an extremely small figure compared to the losses a catastrophic risk would impose on society. And further, only private plaintiffs who have "suffered injury in fact" have standing to sue under UCL. This could make it practically challenging to sue a developer for making false or misleading statements before their model has actually caused a catastrophe.\\
Federal and state securities fraud laws could also ban certain false or misleading statements by developers. It is illegal under [SEC Rule 10b-5](https://www.govinfo.gov/content/pkg/CFR-2014-title17-vol4/pdf/CFR-2014-title17-vol4-sec240-10b-5.pdf) for a corporation "to make any untrue statement of a material fact or to omit to state a material fact necessary in order to make the statements made…not misleading…in connection with the purchase or sale of any security." Rule 10b-5 could be used against developers who make false or misleading claims to investors about their catastrophic risk management. But this legal strategy relies on an untested interpretation of materiality, and it would only apply to public companies or companies actively engaged in selling securities.\\
Overall, it seems likely that paragraph (e) would expand large developers' legal liability for false or misleading safety claims.} about catastrophic risk from its foundation models or its management of catastrophic risk.

(f) (1) When a large developer publishes documents to comply with this section, the large developer may make redactions to those documents that are necessary to protect the large developer’s trade secrets, the large developer’s cybersecurity, public safety, or the national security of the United States or to comply with any federal or state law.

&nbsp;&nbsp;(2) If a large developer redacts information in a document pursuant to this subdivision, the large developer shall describe the character and justification of the redaction in any published version of the document to the extent permitted by the concerns that justify redaction and shall retain the unredacted information for five years.

### 22757.13.

(a) The Attorney General shall [establish a mechanism]{This mechanism could be modeled on the mechanism that the California AG uses to [collect mandatory incident reports](https://oag.ca.gov/privacy/databreach/reporting) from companies that have suffered large data breaches.} to be used by a large developer or a member of the public to report a critical safety incident that includes all of the following:

&nbsp;&nbsp;(1) The date of the critical safety incident.

&nbsp;&nbsp;(2) The reasons the incident qualifies as a critical safety incident.

&nbsp;&nbsp;(3) A short and plain statement describing the critical safety incident.

(b) A large developer shall report any critical safety incident pertaining to one or more of its foundation models to the Attorney General within 15 days of discovering the critical safety incident.

(c) The Attorney General shall review critical safety incident reports submitted by large developers and may review reports submitted by members of the public.

### 22757.14.

(a) A violation of this chapter shall be subject to a civil penalty in an amount not to exceed [dollars ($)]{The amended bill text released on 8 July does not specify a dollar figure.} per violation, unless the violation is willful or reckless, in which case the civil penalty shall be in an amount not to exceed  dollars ($).

(b) The civil penalty shall be assessed in a civil action brought only by the Attorney General.

### 22757.15.

(a) On or before January 1, 2027, and annually thereafter, the Attorney General may adopt regulations to update the definition of a “large developer” for the purposes of this chapter to ensure that it accurately reflects technological developments, scientific literature, and widely accepted national and international standards and applies to well-resourced large developers at the frontier of artificial intelligence development.

(b) In developing regulations pursuant to this section, the Attorney General shall take into account all of the following:

&nbsp;&nbsp;(1) Similar thresholds used in international standards or federal law, guidance, or regulations for the management of catastrophic risk.

&nbsp;&nbsp;(2) Input from stakeholders, including academics, industry, the open-source community, and governmental entities.

&nbsp;&nbsp;(3) The extent to which a person will be able to determine, before beginning to train or deploy a foundation model, whether that person will be subject to the regulations as a large developer with an aim toward allowing earlier determinations if possible.

&nbsp;&nbsp;(4) The complexity of determining whether a person is covered, with an aim toward allowing simpler determinations if possible.

&nbsp;&nbsp;(5) The external verifiability of determining whether a person is covered, with an aim toward definitions that are verifiable by parties other than the large developer.

(c) If the Attorney General determines that less well-resourced developers, or developers significantly behind the frontier of artificial intelligence, may create substantial catastrophic risk, the Attorney General shall promptly submit a report to the Legislature, pursuant to Section 9795, with a proposal for managing this source of catastrophic risk but shall not include those developers within the definition of “large developer” without authorization in subsequently enacted legislation.

## SECTION 3.
Section 11546.8 is added to the Government Code, to read:

### 11546.8. 

(a) There is hereby established within the Government Operations Agency a consortium that shall develop, pursuant to this section, a framework for the creation of a [public cloud computing cluster]{Several other governments have recently established, or are in the process of establishing, public AI compute clusters similar to CalCompute.\\
In 2023, the United Kingdom announced the [AI Research Resource](https://www.ukri.org/news/300-million-to-launch-first-phase-of-new-ai-research-resource), a £300 million fund to pay for publicly owned AI compute clusters. Two public clusters have been announced so far: [Isambard](https://www.bristol.ac.uk/research/centres/bristol-supercomputing/articles/2025/isambard-ai-is-11th-fastest-supercomputer-in-the-world.html) at the University of Bristol and [Dawn](https://www.hpc.cam.ac.uk/d-w-n) at the University of Cambridge. Isambard came online last month, and the UK's Department of Science, Innovation & Technology [recently announced](https://www.gov.uk/government/publications/ai-opportunities-action-plan/ai-opportunities-action-plan) plans to scale up AIRR's clusters by 20x over the next five years.\\
Earlier this year, the European Union announced [InvestAI](https://digital-strategy.ec.europa.eu/en/news/eu-launches-investai-initiative-mobilise-eu200-billion-investment-artificial-intelligence), a €20 billion fund for building publicly owned AI compute in Europe. The fund aims to build three to five "[AI gigafactories](https://digital-strategy.ec.europa.eu/en/policies/ai-factories)", each containing more than 10^5 H100 equivalents, but none of the gigafactories are online yet.\\
At the federal level, the National Science Fuondation is leading a [two-year pilot](https://www.nsf.gov/focus-areas/artificial-intelligence/nairr) of the National AI Research Resource, which provides AI cloud compute for US researchers. NAIRR's [stated goals](https://nairrpilot.org/about) are to "spur innovation, develop workforce talent, improve capacity, and advance safe, secure, and trustworthy AI," overlapping strongly with the goals of CalCompute.} to be known as “CalCompute.”

(b) The consortium shall develop a framework for the creation of CalCompute that advances the development and deployment of artificial intelligence that is safe, ethical, equitable, and sustainable by doing, at a minimum, both of the following:

&nbsp;&nbsp;(1) Fostering research and innovation that benefits the public.

&nbsp;&nbsp;(2) Enabling equitable innovation by expanding access to computational resources.

(c) The consortium shall make reasonable efforts to ensure that CalCompute is established within the [University of California]{The University of California already operates two clusters with substantial AI-relevant compute: the [National Energy Research Scientific Computing Center](https://www.nersc.gov/) at UC Berkeley, and the [San Diego Supercomputer Center](https://www.sdsc.edu/) at UC San Diego.} to the extent possible.

(d) CalCompute shall include, but not be limited to, all of the following:

&nbsp;&nbsp;(1) A fully owned and hosted cloud platform.

&nbsp;&nbsp;(2) Necessary human expertise to operate and maintain the platform.

&nbsp;&nbsp;(3) Necessary human expertise to support, train, and facilitate the use of CalCompute.

(e) The consortium shall operate in accordance with all relevant labor and workforce laws and standards.

(f) (1) On or before January 1, 2027, the Government Operations Agency shall submit, pursuant to Section 9795, a report from the consortium to the Legislature with the framework developed pursuant to subdivision (b) for the creation and operation of CalCompute.

&nbsp;&nbsp;(2) The report required by this subdivision shall include all of the following elements:

&nbsp;&nbsp;&nbsp;&nbsp;(A) A landscape analysis of California’s current public, private, and nonprofit cloud computing platform infrastructure.

&nbsp;&nbsp;&nbsp;&nbsp;(B) An analysis of the cost to the state to build and maintain CalCompute and recommendations for potential funding sources.

&nbsp;&nbsp;&nbsp;&nbsp;(C) Recommendations for the governance structure and ongoing operation of CalCompute.

&nbsp;&nbsp;&nbsp;&nbsp;(D) Recommendations for the parameters for use of CalCompute, including, but not limited to, a process for determining which users and projects will be supported by CalCompute.

&nbsp;&nbsp;&nbsp;&nbsp;(E) An analysis of the state’s technology workforce and recommendations for equitable pathways to strengthen the workforce, including the role of CalCompute.

&nbsp;&nbsp;&nbsp;&nbsp;(F) A detailed description of any proposed partnerships, contracts, or licensing agreements with nongovernmental entities, including, but not limited to, technology-based companies, that demonstrates compliance with the requirements of subdivisions (c) and (d).

&nbsp;&nbsp;&nbsp;&nbsp;(G) Recommendations regarding how the creation and ongoing management of CalCompute can prioritize the use of the current public sector workforce.

(g) The consortium shall, consistent with state constitutional law, consist of 14 members as follows:

&nbsp;&nbsp;(1) Four representatives of the University of California and other public and private academic research institutions and national laboratories appointed by the Secretary of Government Operations.

&nbsp;&nbsp;(2) Three representatives of impacted workforce labor organizations appointed by the Speaker of the Assembly.

&nbsp;&nbsp;(3) Three representatives of stakeholder groups with relevant expertise and experience, including, but not limited to, ethicists, consumer rights advocates, and other public interest advocates appointed by the Senate Rules Committee.

&nbsp;&nbsp;(4) Four experts in technology and artificial intelligence to provide technical assistance appointed by the Secretary of Government Operations.

(h) The members of the consortium shall serve without compensation, but shall be reimbursed for all necessary expenses actually incurred in the performance of their duties.

(i) The consortium shall be dissolved upon submission of the report required by paragraph (1) of subdivision (f) to the Legislature.

(j) If CalCompute is established within the University of California, the University of California may receive private donations for the purposes of implementing CalCompute.

(k) This section shall become operative only upon an appropriation in a budget act, or other measure, for the purposes of this section.

## SECTION 4.
Chapter 5.1 (commencing with Section 1107) is added to Part 3 of Division 2 of the Labor Code, to read:

### CHAPTER  5.1. Whistleblower Protections: Catastrophic Risks in AI Foundation Models

1107. For purposes of this chapter:

(a) “[Artificial intelligence model]{This is exactly the same definition given in §2. Again, it is a close paraphrase of the [OECD's definition](https://www.oecd.org/en/publications/explanatory-memorandum-on-the-updated-oecd-definition-of-an-ai-system_623da898-en.html) of an AI system.}” means an engineered or machine-based system that varies in its level of autonomy and that can, for explicit or implicit objectives, infer from the input it receives how to generate outputs that can influence physical or virtual environments.

(b) "Catastrophic risk" has the meaning defined in Section 22757.11 of the Business and Professions Code.

(c) “Large developer” has the meaning defined in Section 22757.11 of the Business and Professions Code.

(d) “[Employee]{This is a remarkably expansive definition of "employee." Independent contractors, freelancers, and unpaid advisors are usually not treated as employees under normal employment law, but for purposes of this chapter, they do count. This ensures that virtually anyone within a frontier developer who could plausibly access privileged information about catastrophic risks gets whistleblower protection.\\
The [AI Whistleblower Protection Act](https://www.grassley.senate.gov/imo/media/doc/ai_whistleblower_protection_act.pdf) currently up for debate in the US Senate extends protection to a partially overlapping class of individuals. SB 53 goes farther than AIWPA in extending protection to board members and unpaid advsors of large developers, but AIWPA goes farther than SB 53 in extending protection to *former* as well as current employees and contractors.}” means a person who performs services for an employer, including both of the following:

&nbsp;&nbsp;(1) A contractor, subcontractor, or an unpaid advisor involved with assessing, managing, or addressing catastrophic risk, including all of the following:

&nbsp;&nbsp;&nbsp;&nbsp;(A) An independent contractor.

&nbsp;&nbsp;&nbsp;&nbsp;(B) A freelance worker.

&nbsp;&nbsp;&nbsp;&nbsp;(C) A person employed by a labor contractor.

&nbsp;&nbsp;&nbsp;&nbsp;(D) A board member.

&nbsp;&nbsp;(2) Corporate officers.

(e) “Foundation model” has the same meaning as defined in Section 22757.11 of the Business and Professions Code.

(f) “Labor contractor” means an individual or entity that supplies, either with or without a contract, a client employer with workers to perform labor within the client employer’s usual course of business.

1107.1. (a) A large developer shall not make, adopt, enforce, or enter into a rule, regulation, policy, or contract that prevents an employee from disclosing, or retaliates against an employee for disclosing, information to the Attorney General, a federal authority, a person with authority over the employee, or another employee who has authority to investigate, discover, or correct the reported issue, if the employee has reasonable cause to believe that the information discloses either of the following:

&nbsp;&nbsp;(1) The large developer’s activities pose a catastrophic risk.

&nbsp;&nbsp;(2) The large developer has violated Chapter 25.1 (commencing with Section 22757.10) of Division 8 of the Business and Professions Code.

(b) A large developer shall not enter into a contract that prevents an employee from making a [disclosure protected under Section 1102.5.]{[§1102.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=1102.5) of the California Labor Code says that an employer may not make a rule against employees disclosing violations of federal, state, or local law to public officials or to their superiors. Further, it forbids an employer from retaliating against an employee who makes such a disclosure.}

(c) A large developer shall not make, adopt, enforce, or enter into a rule, regulation, policy, or contract that would prevent an [organization or entity]{This could include third-party model evaluators who test AI systems for dangerous capabilities or tendencies. Some prominent model evaluators include the [UK AI Security Institute](https://www.aisi.gov.uk/), [METR](https://metr.org/), and [Apollo Research](https://www.apolloresearch.ai/).} that provides goods or services to the large developer related to the assessment, management, or addressing of catastrophic risk, or an employee of that organization or entity, from disclosing information to the Attorney General, a federal authority, or the developer if the organization, entity, or individual has reasonable cause to believe that the information discloses either of the following:

&nbsp;&nbsp;(1) The large developer’s activities pose a catastrophic risk.

&nbsp;&nbsp;(2) The large developer has violated Chapter 25.1 (commencing with Section 22757.10) of Division 8 of the Business and Professions Code.

(d) An employee may use the hotline described in Section 1102.7 to make reports described in subdivision (a).

(e) A large developer shall provide a clear notice to all employees of their rights and responsibilities under this section, including by doing either of the following:

&nbsp;&nbsp;(1) At all times posting and displaying within any workplace maintained by the large developer a notice to all employees of their rights under this section, ensuring that any new employee receives equivalent notice, and ensuring that any employee who works remotely periodically receives an equivalent notice.

&nbsp;&nbsp;(2) At least once each year, providing written notice to each employee of the employee’s rights under this section and ensuring that the notice is received and acknowledged by all of those employees.

(f) (1) A large developer shall provide a reasonable internal process through which an employee may anonymously disclose information to the large developer if the employee believes in good faith that the information indicates that the large developer’s activities present a catastrophic risk or that the large developer has violated Chapter 25.1 (commencing with Section 22757.10) of Division 8 of the Business and Professions Code, including a monthly update to the person who made the disclosure regarding the status of the large developer’s investigation of the disclosure and the actions taken by the large developer in response to the disclosure.

&nbsp;&nbsp;(2) (A) Except as provided in subparagraph (B), the disclosures and responses of the process required by this subdivision shall be shared with officers and directors of the large developer at least once each quarter.

&nbsp;&nbsp;&nbsp;&nbsp;(B) If an employee has alleged wrongdoing by an officer or director of the large developer in a disclosure or response, subparagraph (A) shall not apply with respect to that officer or director.

(g) The court is authorized to award reasonable attorney’s fees to a plaintiff who brings a successful action for a violation of this section.

(h) In a civil action brought pursuant to this section, once it has been demonstrated by a preponderance of the evidence that an activity proscribed by this section was a contributing factor in the alleged prohibited action against the employee, the large developer shall have the burden of proof to demonstrate by clear and convincing evidence that the alleged action would have occurred for legitimate, independent reasons even if the employee had not engaged in activities protected by this section.

(i) (1) In a civil action or administrative proceeding brought pursuant to this section, an employee may petition the superior court in any county wherein the violation in question is alleged to have occurred, or wherein the person resides or transacts business, for appropriate temporary or preliminary injunctive relief.

&nbsp;&nbsp;(2) Upon the filing of the petition for injunctive relief, the petitioner shall cause notice thereof to be served upon the person, and thereupon the court shall have jurisdiction to grant temporary injunctive relief as the court deems just and proper.

&nbsp;&nbsp;(3) In addition to any harm resulting directly from a violation of this section, the court shall consider the chilling effect on other employees asserting their rights under this section in determining whether temporary injunctive relief is just and proper.

&nbsp;&nbsp;(4) Appropriate injunctive relief shall be issued on a showing that reasonable cause exists to believe a violation has occurred.

&nbsp;&nbsp;(5) An order authorizing temporary injunctive relief shall remain in effect until an administrative or judicial determination or citation has been issued, or until the completion of a review pursuant to subdivision (b) of Section 98.74, whichever is longer, or at a certain time set by the court. Thereafter, a preliminary or permanent injunction may be issued if it is shown to be just and proper. Any temporary injunctive relief shall not prohibit a large developer from disciplining or terminating an employee for conduct that is unrelated to the claim of the retaliation.

(j) Notwithstanding Section 916 of the Code of Civil Procedure, injunctive relief granted pursuant to this section shall not be stayed pending appeal.

(k) (1) This section does not impair or limit the applicability of Section 1102.5.

&nbsp;&nbsp;(2) The remedies provided by this section are cumulative to each other and the remedies or penalties available under all other laws of this state.

## SECTION 5.

(a) The provisions of this act are severable. If any provision of this act or its application is held invalid, that invalidity shall not affect other provisions or applications that can be given effect without the invalid provision or application.

(b) This act shall be liberally construed to effectuate its purposes.

(c) The duties and obligations imposed by this act are cumulative with any other duties or obligations imposed under other law and shall not be construed to relieve any party from any duties or obligations imposed under other law and do not limit any rights or remedies under existing law.

(d) This act shall not apply to the extent that it strictly conflicts with the terms of a contract between a federal government entity and a large developer.

(e) This act shall not apply to the extent that it is preempted by federal law.