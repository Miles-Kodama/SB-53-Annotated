# California Senate Bill 53
This site presents the text of Senate Bill 53 enriched with background and commentary. Click on any of the blue highlights to learn more. The bill text below was last amended on 17 July, 2025.

## SECTION 1.
The Legislature finds and declares all of the following:

(a) California is leading the world in artificial intelligence innovation and research through companies large and small and through the state’s remarkable public and private universities.

(b) Artificial intelligence, including new advances in foundation models, has the potential to catalyze innovation and the rapid development of a wide range of benefits for Californians and the California economy, including advances in medicine, wildfire forecasting and prevention, and climate science, and to push the bounds of human creativity and capacity.

(c) The [Joint California Policy Working Group]{This refers to a group of AI experts [convened](https://www.gov.ca.gov/2024/09/29/governor-newsom-announces-new-initiatives-to-advance-safe-and-responsible-ai-protect-californians/) by Governor Gavin Newsom in September 2024 to study how California should govern frontier AI. The Working Group was led by Stanford HAI co-director [Fei-Fei Li](https://hai.stanford.edu/people/fei-fei-li), Carnegie Endowment president [Tino Cuéllar](https://carnegieendowment.org/people/mariano-florentino-tino-cuellar?lang=en), and UC Berkeley professor [Jennifer Chayes](https://cdss.berkeley.edu/people/jennifer-chayes). They published their findings in June 2025 as the [California Report on Frontier AI Policy.](https://www.cafrontieraigov.org/)\\
SB 53's content draws heavily upon the California Report's recommendations, [as noted](https://sd11.senate.ca.gov/news/senator-wiener-expands-ai-bill-landmark-transparency-measure-based-recommendations-governors) by the bill's author, Senator Scott Wiener.} on AI Frontier Models has recommended sound principles for policy in artificial intelligence.

(d) Targeted interventions to support effective artificial intelligence governance should balance the technology’s benefits and material risks.

(e) Artificial intelligence developers [have already voluntarily committed]{At the 2024 AI Summit in Seoul, most of America's leading AI companies voluntarily agreed to the [Frontier AI Safety Commitments](https://www.gov.uk/government/publications/frontier-ai-safety-commitments-ai-seoul-summit-2024/frontier-ai-safety-commitments-ai-seoul-summit-2024). Under these commitments each signatory must make a plan to assess and manage any severe risks their systems could pose (outcome 1), and they must disclose the results of their risk assessments to their home government (outcome 3). OpenAI, Anthropic, Google, xAI, Meta, Microsoft, and Amazon are all signatories to the Seoul Commitments\\
Previously in 2023, top American AI developers agreed to the [White House Voluntary Commitments on AI](https://bidenwhitehouse.archives.gov/briefing-room/statements-releases/2023/07/21/fact-sheet-biden-harris-administration-secures-voluntary-commitments-from-leading-artificial-intelligence-companies-to-manage-the-risks-posed-by-ai/). These developers committed to running pre-deployment safety and security tests on their models, including tests by external experts. They also committed to issuing public reports on their AI systems' "capabilities, limitations, and areas of appropriate and inappropriate use." The White House Commitments are not legally binding regulations, and they rely on AI developers to self-enforce. OpenAI, Anthropic, Google, Meta, Microsoft, and Amazon all agreed to the White House Commitments.} to creating safety and security protocols and releasing the results of risk assessments.

(f) In building a robust and transparent evidence environment, policymakers can align incentives to simultaneously protect consumers, leverage industry expertise, and recognize leading safety practices.

(g) When industry actors conduct internal research on their technologies’ impacts, a significant information asymmetry can develop between those with privileged access to data and the broader public.

(h) Greater transparency, given current information deficits, can advance accountability, competition, and public trust.

(i) Whistleblower protections and public-facing information sharing are key instruments to increase transparency.

(j) [Adverse event reporting systems]{Much like the FDA's [Adverse Event Reporting System](https://www.fda.gov/drugs/surveillance/fdas-adverse-event-reporting-system-faers), a database that records adverse symptoms suffered by patients on FDA-approved drugs. FAERS exists to help drug regulators identify rare or long-latency effects of drugs that might not have been detected in pre-market clinical trials.\\
Similarly, adverse event reporting systems for AI could help AI regulators identify undesirable properties of models that might not have been caught in pre-deployment safety testing.} enable monitoring of the post-deployment impacts of artificial intelligence.

(k) There is growing evidence that, unless they are developed with careful diligence and reasonable precaution, advanced artificial intelligence systems [could pose catastrophic risks]{For an overview of the evidence that advanced AI could pose catastrophic risks, see §2 of the [International AI Safety Report](https://www.gov.uk/government/publications/international-ai-safety-report-2025/international-ai-safety-report-2025#risks).} from both malicious uses and malfunctions, including [artificial intelligence-enabled hacking]{Evaluations indicate that current models are still too weak at offensive hacking to substantially uplift competent threat actors (see [Rodriguez et al.](https://deepmind.google/discover/blog/evaluating-potential-cybersecurity-threats-of-advanced-ai/)), but this could change as frontier models gain more advanced [coding skills](https://epoch.ai/data/ai-benchmarking-dashboard) and [autonomy](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/).}, [biological attacks]{There has not yet been a documented bio attack meaningfully assisted by AI, but frontier LLMs already [exceed human expert performance](https://arxiv.org/abs/2505.06108) on tests of dangerous biology knowledge, and their biology skills continue to improve.\\
The [California Report](https://www.cafrontieraigov.org/) (§1.3) notes that "improvements in capabilities across frontier AI models and companies tied to biology are especially striking. For example, OpenAI’s o3 model outperforms 94% of expert virologists… Claude 4 Opus has demonstrated similar CBRN-related capabilities, including helping users access dual-use biological knowledge"}, and [loss of control]{Loss of control generally refers to scenarios where an AI system autonomously takes actions against its user's intent or wishes, and the user cannot correct the system or shut it down.}.

(l) With the frontier of artificial intelligence rapidly evolving, there is a need for legislation to track the frontier of artificial intelligence research and alert policymakers and the public to the risks and harms from the very most advanced artificial intelligence systems, while avoiding burdening smaller companies behind the frontier.

(m) In the future, foundation models developed by [smaller companies or that are behind the frontier]{The main reason why companies behind the frontier could eventually pose catastrophic risk is algorithmic progress. Every year, machine learning researchers discover new ways to make their learning algorithms more efficient, allowing them to train a model with a given level of performance using fewer FLOPS than previously would have been needed. Epoch AI have estimated the rate of algorithmic progress for language models, and [they find](https://epoch.ai/blog/algorithmic-progress-in-language-models) that from 2012 to 2023, the FLOPS required to achieve some fixed level of performance halved every eight months. If this trend holds, a model that takes 10^26 FLOPs to train now will take two orders of magnitude fewer FLOPs in five years.} may pose significant catastrophic risk, and additional legislation may be needed at that time.

(n) It is the intent of the Legislature to create more transparency, but collective safety will depend in part on large developers taking due care in their development and deployment of foundation models proportional to the scale of the foreseeable risks.

## SECTION 2.
Chapter 25.1 (commencing with Section 22757.10) is added to Division 8 of the Business and Professions Code, to read:

### CHAPTER  25.1. Transparency in Frontier Artificial Intelligence Act

### 22757.10.

This chapter shall be known as the Transparency in Frontier Artificial Intelligence Act.

### 22757.11.

For purposes of this chapter:

(a) “[Artificial intelligence model]{This definition is a close paraphrase of the [OECD's definition](https://www.oecd.org/en/publications/explanatory-memorandum-on-the-updated-oecd-definition-of-an-ai-system_623da898-en.html) of an AI system, published in March 2024.}” means an engineered or machine-based system that varies in its level of autonomy and that can, for explicit or implicit objectives, infer from the input it receives how to generate outputs that can influence physical or virtual environments.

(b) “Catastrophic risk” means a foreseeable and material risk that a large developer’s development, storage, use, or deployment of a foundation model will materially contribute to the death of, or serious injury to, more than [50 people]{An AI model could materially contribute to a mass casualty event by, for example, helping a bioterrorist to [create a dangerous pathogen](https://ai-frontiers.org/articles/ais-are-disseminating-expert-level-virology-skills) or carrying out a [cyberattack on critical infrastructure](https://safe.ai/blog/cybersecurity-and-ai-the-evolving-security-landscape).} or more than [one billion dollars]{An AI model could materially contribute to a billion dollars of economic loss by assisting in the creation or release of a pathogen that causes a major epidemic. The economic cost of the COVID-19 pandemic is estimated at [over ten trillion dollars](https://pmc.ncbi.nlm.nih.gov/articles/PMC7604733/), so even an epidemic four orders of magnitude less severe would count as catastrophic by this definition. A model could also cause a billion dollars of loss through mass cybercrime, for instance, by spreading [self-replicating ransomware](https://www.wired.com/story/notpetya-cyberattack-ukraine-russia-code-crashed-the-world/) or by [autonomously scamming](https://metr.org/blog/2024-11-12-rogue-replication-threat-model/) people on a massive scale.} ($1,000,000,000) in damage to, or loss of, property arising from a single incident, scheme, or course of conduct involving a dangerous capability.

(c) “Critical safety incident” means any of the following:

&nbsp;&nbsp;(1) Unauthorized access to, modification of, or exfiltration of, the model weights of a foundation model.

&nbsp;&nbsp;(2) Harm resulting from the materialization of a catastrophic risk.

&nbsp;&nbsp;(3) Loss of control of a foundation model causing death, bodily injury, or damage to, or loss of, property.

&nbsp;&nbsp;(4) A foundation model that uses [deceptive techniques]{For instance, a model could hide its true desires and motivations from its developers in hopes of protecting those desires from modification. [Greenblatt et al.](https://www.anthropic.com/research/alignment-faking) observed this behavior in Claude 3 Opus in their "Alignment Faking in Large Language Models" experiment.\\
A model might also intentionally underperform on capabilities tests, either because it was deliberately trained to do so by its developers, or because the model wants to hide its full capabilities from its own developers. This behavior is usually called "sandbagging," and [van der Weij et al.](https://arxiv.org/abs/2406.07358v2) have demonstrated that frontier models were already capable of sophisticated sandbagging in mid-2024.\\
The [California Report](https://www.cafrontieraigov.org/) (§1.4) concluded that there is already substantial evidence for models practicing strategic deception, writing "recent models from many AI companies have also demonstrated increased evidence of alignment scheming… and reward hacking… New evidence suggests that models can often detect when they are being evaluated, potentially introducing the risk that evaluations could underestimate harm new models could cause once deployed in the real world."\\
For a theoretical account of why we should expect deceptive behavior to emerge in powerful AI systems, see Joe Carlsmith's report on "[Scheming AIs: Will AIs fake alignment during training in order to get power?](https://joecarlsmith.com/2023/11/15/new-report-scheming-ais-will-ais-fake-alignment-during-training-in-order-to-get-power)".} against the large developer to subvert the controls or monitoring of its large developer outside of the context of an evaluation designed to elicit this behavior.

&nbsp;&nbsp;(5) Attaining a dangerous capability or catastrophic risk threshold, as defined in the large developers safety and security protocol pursuant to paragraph (3) of subdivision (a) of Section 22757.12, for the first time.

(d) “[Dangerous capability]{This definition of dangerous capabilities aligns with definitions found in the scientific literature. See, for instance, foundational papers by [Phuong et al.](https://deepmind.google/research/publications/78150/) and [Shevlane et al.](https://www.governance.ai/research-paper/model-evaluation-for-extreme-risks), as well as the recent [California Report](https://www.cafrontieraigov.org/).\\
The ability to persuade or manipulate humans is also sometimes considered a dangerous model capability. Capabilities (3) and (4) below could implicitly include dangerous persuasion.}” means the capacity of a foundation model to do any of the following:

&nbsp;&nbsp;(1) Provide expert-level assistance in the creation or release of a chemical, biological, radiological, or nuclear weapon.

&nbsp;&nbsp;(2) Conduct or assist in a cyberattack.

&nbsp;&nbsp;(3) Engage in conduct, with limited human intervention, that would, if committed by a human, constitute the crime of murder, assault, extortion, or theft, including theft by false pretense.

&nbsp;&nbsp;(4) Evade the control of its large developer or user.

(e) (1) “[Deploy]{This definition counts both closed source releases—where users are allowed to query a model only through a web app or API—and open source releases—where users are given full access to a model's weights—as deployments.}” means to make a foundation model available to a third party for use, modification, copying, or combination with other software.

&nbsp;&nbsp;(2) “Deploy” does not include making a foundation model available to a third party for the primary purpose of developing or evaluating the foundation model.

(f) “[Foundation model]{There is no uniform definition of "foundation model" found in the scientific literature. Some authors exclude the host, scaffold, and application from their definitions of a foundation model. On these definitions, GPT-4 would count as a foundation model, but the ChatGPT application built atop GPT-4 would not count. SB 53 instead uses a wider definition, treating the host, scaffold, and application all as part of a foundation model. For more, see "[What is a Foundation Model?](https://www.adalovelaceinstitute.org/resource/foundation-models-explainer/)" from the Ada Lovelace Institute.}” means an artificial intelligence model that is all of the following:

&nbsp;&nbsp;(1) Trained on a broad data set.

&nbsp;&nbsp;(2) Designed for generality of output.

&nbsp;&nbsp;(3) Adaptable to a [wide range of distinctive tasks]{This apparently counts large language models like OpenAI's GPT series but excludes narrow AI models like Google DeepMind's [AlphaFold](https://deepmind.google/science/alphafold/) or OpenAI [Five](https://openai.com/index/openai-five-defeats-dota-2-world-champions/).}.

(g) “[Large developer]{SB 53 takes an [entity-based](https://carnegieendowment.org/research/2025/06/artificial-intelligence-regulation-united-states) approach to AI regulation. Instead of regulating frontier models—as SB 1047 would have done—SB 53 regulates large developers. This entity-based approach may prove more robust than model-based approaches to unforeseen technical innovations. Model-based regulation requires regulators to set a threshold that determines which models are at the frontier, but such thresholds can rapidly become obsolete when training paradigms change. On the other hand, entity-based regulation avoids inadvertently burdening small or behind-the-frontier AI developers in the future because their models pass a threshold that *used* to indicate frontier capabilities.\\
New York's proposed [RAISE Act](https://www.nysenate.gov/legislation/bills/2025/A6453/amendment/A) is another prominent instance of entity-based AI regulation.}” means either of the following:

&nbsp;&nbsp;(1) (A) Before January 1, 2027, “large developer” means a person who meets both of the following criteria:

&nbsp;&nbsp;&nbsp;&nbsp;(i) (I) The person has trained, or initiated the training of, at least one foundation model using a quantity of computing power greater than [10^26 integer or floating point operations]{According to [Epoch AI's estimates](https://epoch.ai/data/notable-ai-models), no company had ever published a foundational model above this threshold until early 2025. Since then, only two companies (OpenAI and xAI) have released models that pass the threshold.\\
President Biden's [Executive Order 14110](https://www.govinfo.gov/content/pkg/FR-2023-11-01/pdf/2023-24283.pdf) also used 10^26 training FLOPs as the threshold for a frontier model. Under EO 14110, any developer training a model above the threshold was required to disclose their safety testing results and security protocols to Federal authorities.}

&nbsp;&nbsp;&nbsp;&nbsp; (II) The quantity of computing power described in subparagraph (A) subclause (I) shall include computing for the original training run and any [subsequent fine-tuning, reinforcement learning, or other material modifications]{Fine-tuning and RL are often referred to as "post-training", a catch-all for the adjustments AI companies make to a model after an initial pre-training run. Post-training already consumes a significant share of a frontier training run's compute budget. [xAI claims](https://www.interconnects.ai/p/grok-4-an-o3-look-alike-in-search) that more than half of the FLOPs used to train Grok 4 were spent on RL. If this is true, Grok 4's post-training compute already surpasses the 10^26 FLOP threshold, even without counting pre-training compute.\\
It's expected that future frontier runs will allocate an even larger share of their compute to post-training, as AI companies continue [teaching their models to reason](https://benjamintodd.substack.com/p/teaching-ai-to-reason-this-years) through chain of thought RL.} to a preceding foundation model.

&nbsp;&nbsp;&nbsp;&nbsp;(ii) The person had annual gross revenues in excess of [one hundred million dollars]{Both of the AI developers known to have trained a model with over 10^26 FLOPs also meet this criterion. [X](https://en.wikipedia.org/wiki/X_Corp.)'s revenue in 2024 was $2.7 billion, and [OpenAI](https://www.wsj.com/tech/ai/openaiin-talks-for-huge-investment-round-valuing-it-up-to-300-billion-2a2d4327)'s revenue is estimated to have been $3.7 billion. Other leading AI developers who could plausibly soon train a model with over 10^26 FLOPs—such as [Anthropic](https://www.reuters.com/business/anthropic-hits-3-billion-annualized-revenue-business-demand-ai-2025-05-30/), [Google](https://abc.xyz/assets/a3/91/6d1950c148fa84c7d699abe05284/2024q4-alphabet-earnings-release.pdf), and [Meta](https://investor.atmeta.com/investor-news/press-release-details/2025/Meta-Reports-Fourth-Quarter-and-Full-Year-2024-Results/)—also exceed $100 million in annual revenue.} ($100,000,000) in the preceding calendar year.

&nbsp;&nbsp;(2) (A) Except as provided in subparagraph (B), on and after January 1, 2027, “large developer” has the meaning defined by a regulation adopted by the Attorney General pursuant to Section 22757.15.

&nbsp;&nbsp;&nbsp;&nbsp;(B) If the Attorney General does not adopt a regulation described in subparagraph (A) by January 1, 2027, the definition in paragraph (1) shall be operative until the regulation is adopted.

(h) “[Model weight]{The model weights, when combined with facts about the model architecture, encode all the information required to run a model. A user who has the weights can get the model's response to any query they want, even a dangerous query that would have been blocked by the developer's [guardrails](https://www.anthropic.com/news/constitutional-classifiers). Moreover, anyone who has access to the weights can easily modify the model to undo alignment and refusal training, as demonstrated by [Gade et al.](https://arxiv.org/abs/2311.00117) and [Arditi et al.](https://arxiv.org/abs/2406.11717). If malicious actors can steal the weights of frontier models, they might therefore be able to use the model to cause a catastrophe.}” means a numerical parameter in a foundation model that is adjusted through training and that helps determine how inputs are transformed into outputs.

(i) "Property" means tangible or intangible property.

(j) “Safety and security protocol” means documented technical and organizational protocols to manage, assess, and mitigate catastrophic risks.

### 22757.12.

(a) A large developer shall write, implement, comply with, and clearly and conspicuously publish on its internet website a [safety and security protocol]{Many leading AI developers have already written and published documents similar to the safety and security policies that SB 53 calls for. These documents can go by many different names, including "frontier safety policy", "responsible scaling policy", and "preparedness framework". On a high level, each safety protocol describes how an AI developer plans to identify, measure, and mitigate the risks that its systems create.\\
For an overview of existing safety protocols, see the Frontier Model Forum's [issue brief](https://www.frontiermodelforum.org/updates/issue-brief-components-of-frontier-ai-safety-frameworks/) or METR's report on "[Common Elements of Frontier AI Safety Policies](https://metr.org/blog/2025-03-26-common-elements-of-frontier-ai-safety-policies/)".} that describes in specific detail all of the following:

&nbsp;&nbsp;(1) How, if at all, the large developer [excludes certain foundation models]{Most likely, none of the frontier AI developers are yet in compliance with this provision.
* Anthropic's [Responsible Scaling Policy](https://www-cdn.anthropic.com/f3b282f157017d08e36636bda1bf3bd4d9f23ee7.pdf) only applies to "frontier AI models," but the policy does not explain how Anthropic decides which of their models count as frontier models.
* OpenAI's [Preparedness Framework](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) (§3.2) applies only to models with a "plausible chance" of reaching a new capability threshold. OpenAI does not describe their process for deciding whether a chance is plausible. 
* Google DeepMind's [Frontier Safety Framework](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/updating-the-frontier-safety-framework/Frontier%20Safety%20Framework%202.0.pdf) only requires Google to run dangerous capability evaluations on their "most powerful frontier models," and it only calls for safety mitigations to be placed on models that score highly on dangerous capability evals. It is unclear how Google decides whether a model is among their most powerful frontier models.
* xAI has yet to publish an official safety policy. The "Scope" section of their [draft safety policy](https://x.ai/documents/2025.02.20-RMF-Draft.pdf) apparently says that all of xAI's future AI systems are covered by the policy.} from being covered by its safety and security protocol because those foundation models are incapable of posing material catastrophic risks and which foundation models, if any, have been included.

&nbsp;&nbsp;(2) The [testing procedures]{Many large developers discuss the testing procedures they use to assess catastrophic risks in their existing safety policies. Some of them may already be in compliance with this provision.
* Anthropic's [Responsible Scaling Policy](https://www-cdn.anthropic.com/f3b282f157017d08e36636bda1bf3bd4d9f23ee7.pdf) (§§2,3) says that Anthropic will test each of their models for dangerous capabilities related to chemical, biological, radiological, and nuclear weapons and autonomous AI R&D. These dangerous capability results then determine the strictness of the safeguards and security measures Anthropic applies to their models.
* OpenAI's [Preparedness Framework](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) (§§2,3) divides dangerous model capabilities into two groups, tracked capability categories and research capbility categories. Broadly, the tracked categories (§2.2) are more easily measurable or tie into better established threat models. OpenAI's tracked categories are biological and chemical capabilities, cybersecurity capabilities, and AI self-improvement. The research categories are broadly capabilities that OpenAI considers harder to measure or more speculative, and they include long-range autonomy, sandbagging, [autonomous replication and adaptation](https://arxiv.org/abs/2312.11671), undermining safeguards, and nuclear and radiological capabilities. The Framework states that OpenAI tests every frontier model they develop for capabilities in the tracked categories and uses the results to assess the risks posed by the model.
* Google DeepMind's [Frontier Safety Framework](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/updating-the-frontier-safety-framework/Frontier%20Safety%20Framework%202.0.pdf) says that Google will test their frontier models for dangerous capabilities related to both misuse risk and deceptive alignment risk. The capabilities Google intends to measure related to misuse include chemical, biological, radiological, and nuclear capabilities, cyber capabilities, and machine learning R&D. The only capability Google names related to deceptive alignment risk is instrumental reasoning. The results of all these dangerous capability tests are then used to assess how much risk a model poses.
* xAI has yet to publish an official safety policy. Their [draft safety policy](https://x.ai/documents/2025.02.20-RMF-Draft.pdf#page=2) (§1) says that xAI intends to test their models' biological, chemical, and cyber capabilities by running benchmarks such as [VCT](https://www.virologytest.ai/) and [WMD Proxy](https://www.wmdp.ai/).} that the large developer uses to assess catastrophic risks from its foundation models, including risk resulting from malfunctions, misuse, and foundation models evading the control of the large developer or user.

&nbsp;&nbsp;(3) (A) [Thresholds used by the large developer]{Many frontier developers' existing safety policies specify dangerous capability or risk thresholds and say how they will respond to thresholds being attained. Most of them are plausibly already in compliance with this provision.
* Anthropic's [Responsible Scaling Policy](https://www-cdn.anthropic.com/f3b282f157017d08e36636bda1bf3bd4d9f23ee7.pdf) specifies in detail how they will update their AI Security Levels (ASLs) when their models surpass capability thresholds related to CBRN and autonomous AI R&D.
* OpenAI's [Preparedness Framework](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) explains how OpenAI will determine whether a model has High or Critical capabilities in one of their three tracked categories of dangerous capabilities: biological and chemical, cybersecurity, and AI self-improvement. The Framework also describes, for each dangerous capability threshold, what security measures and safegoards OpenAI would put in place if a model reached that threshold.
* Google DeepMind's [Frontier Safety Framework](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/updating-the-frontier-safety-framework/Frontier%20Safety%20Framework%202.0.pdf) defines Critical Capability Levels for three dangerous domains: CBRN, cyber, and machine learning R&D. The Framework goes on to specify what risk mitigations Google would impose if a frontier model surpassed one of these Critical Capability Levels.
* xAI has yet to publish an official safety policy. Their [draft safety policy](https://x.ai/documents/2025.02.20-RMF-Draft.pdf) does not specify any capability thresholds that would trigger a response from xAI.} to identify and assess whether a foundation model has attained a dangerous capability or poses a catastrophic risk.

&nbsp;&nbsp;&nbsp;&nbsp;(B) How the large developer will assess whether a threshold described in subparagraph (A) has been attained, which may include multiple tiered thresholds for different dangerous capabilities or for catastrophic risk.

&nbsp;&nbsp;&nbsp;&nbsp;(C) The actions the large developer will take if each threshold is attained.

&nbsp;&nbsp;(4) The [mitigations]{Many large developers discuss catastrophic risk mitigations in their existing safety policies. Some of them may already be in compliance with this provision.
* Anthropic's [Responsible Scaling Policy](https://www-cdn.anthropic.com/f3b282f157017d08e36636bda1bf3bd4d9f23ee7.pdf#page=12) (§4.1) describes the mitigations they will put in place upon deploying an [ASL-3 model](https://www.anthropic.com/news/activating-asl3-protections) to prevent the model's capabilities from being misused. The Policy calls for Anthropic to take a "defense in depth" strategy, layering many mechanisms to catch attempted misuse on top of one another, and to rapidly patch jailbreaks and other vulnerabilities when they become known. It also says Anthropic will "prespecify empirical evidence" that would show their deployment mitigations are keeping risk to an acceptable level, though the Policy itself does not specify the nature of this evidence.
* OpenAI's [Preparedness Framework](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) (§4) outlines the safeguards they will apply to models that cross their dangerous capability thresholds. The safeguards put on a model will depend on which capability thresholds the model crosses, and they are intended to reduce risks both from misuse by a malicious user and from misaligned models acting autonomously. OpenAI's list of safeguards includes refusal training, usage monitoring, and tiered access to prevent malicious misuse, as well as alignment training, autonomy hobbling, and automated oversight to prevent attacks by misaligned models. OpenAI's Safety Advisory Group—an internal committee responsible for enforcing the Preparedness Framework—is tasked with assessing whether the safeguards OpenAI has put on a model are reducing risk to an acceptable level. The Group makes this assessment on the basis of evaluations, threat modeling, and a review of the baseline risk caused by other developers' models, and they explain their reasoning in an internal report. 
* Google DeepMind's [Frontier Safety Framework](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/updating-the-frontier-safety-framework/Frontier%20Safety%20Framework%202.0.pdf#page=4) says that they will mitigate the risk caused by their systems through both security and deployment mitigations. Google's security mitigations will be inspired by security principles recommended in RAND's [Securing AI Model Weights](https://www.rand.org/pubs/research_reports/RRA2849-1.html) report, but the Framework does not describe any concrete security measures to be implemented. Google's deployment mitigations will include "safety fine-tuning, misuse filtering and detection, and response protocols," and Google will assess how effective these mitgations are "through assurance evaluations and threat modeling research."
* xAI has yet to publish an official safety policy. Their [draft safety policy](https://x.ai/documents/2025.02.20-RMF-Draft.pdf#page=3) (§2) says they "may potentially utilize" deployment mitigations such as refusal training, circuit breakers, and input and output filtering. The draft policy says xAI will use benchmarks to assess the effectiveness of their safety mitigations, but it does not name specific benchmarks nor set threshold scores that would be considered safe.} that a large developer takes to reduce a catastrophic risk and how the large developer assesses the effectiveness of those mitigations.

&nbsp;&nbsp;(5) The degree to which the large developer’s assessments of catastrophic risk and dangerous capabilities and the effectiveness of catastrophic risk mitigations are [reproducible by external entities]{So far, no frontier AI developer is plausibly in compliance with this provision.}.

&nbsp;&nbsp;(6) The extent to which, and how, a large developer will [use third parties to assess]{It's hard to say which frontier developers are already in compliance with this provision. Many existing frontier safety policies do discuss external evaluators' role in the developer's risk assessment process, but it's unclear which policies (if any) disclose as much as this provision requires. 
* Anthropic's [Responsible Scaling Policy](https://www-cdn.anthropic.com/f3b282f157017d08e36636bda1bf3bd4d9f23ee7.pdf) says they "will solicit input from external experts in relevant domains in the process of developing and conducting capability and safeguards assessments" and that they "may also solicit external expert input prior to making final decisions on the capability and safeguards assessments" (§7.2). The Policy further says that external experts will help Anthropic determine when to activate [ASL-3 security standards](https://www.anthropic.com/news/activating-asl3-protections) and help them verify that they have achieved ASL-3 standards (§§3.3 & 4.3).
* OpenAI's [Preparedness Framework](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf#page=14) says they will work with third parties to further evaluate a model's dangerous capabilities "if we deem that a deployment warrants deeper testing of [those capabilities]." Similarly, OpenAI says they will have third parties assess their deployment safeguards if they deem it necessary and "if high quality third-party testing is available." they also allow their Safety Advisory Group—the internal committee responsible for enforcing the Preparedness Framework—may solicit independent expert advice if they wish. (All of these commitments are in §5.2 of the Framework.)
* Google Deepmind's [Frontier Safety Framework](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/updating-the-frontier-safety-framework/Frontier%20Safety%20Framework%202.0.pdf) says relatively little about how they will use third parties to manage risk. The Framework says Google "may use additional external evaluators to test a model for relevant capabilities, if evaluators with relevant expertise are needed to provide an additional signal about a model’s proximity to [dangerous capability thresholds]." They will also consult external experts "as needed" to assess how close a model is to a dangerous capability threshold and analyze the risk that it poses.
* xAI has yet to publish an official safety policy. Their [draft safety policy](https://x.ai/documents/2025.02.20-RMF-Draft.pdf) says they will test Grok's safeguards by subjecting the model to "qualified external red teams," and otherwise, it makes no mention of third party assessment.} catastrophic risks and dangerous capabilities and the effectiveness of mitigations of catastrophic risk.

&nbsp;&nbsp;(7) The large developer’s [cybersecurity practices]{This provision follows a recommendation in the [California Report](https://www.cafrontieraigov.org/). The Report called for improved "transparency into the cybersecurity practices of model developers, namely their ability to secure unreleased model weights from both company-internal and company-external exfiltration" (§3.1).\\
Many frontier AI developers are already plausibly in compliance with this provision.
* Anthropic's [Responsible Scaling Policy](https://www-cdn.anthropic.com/f3b282f157017d08e36636bda1bf3bd4d9f23ee7.pdf#page=12) (§4.1) describes in detail how Anthropic implements their "ASL-3 Security Standard" to guard their frontier model weights. The ASL-3 Standard has been in force at Anthropic [since May 2025](https://www.anthropic.com/news/activating-asl3-protections). 
* OpenAI's [Preparedness Framework](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf#page=21) (§C.3) describes their planned model weight security practices in detail. The Framework does not state when OpenAI plans to implement these security practices, saying only that they will be in place for "high capability models."
* Google Deepmind's [Frontier Safety Framework](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/updating-the-frontier-safety-framework/Frontier%20Safety%20Framework%202.0.pdf) (table 1) states, in general terms, what security controls they will have in place by the time their leading models reach certain dangerous capability thresholds.
* xAI has yet to publish an official safety policy, and their [draft safety policy](https://x.ai/documents/2025.02.20-RMF-Draft.pdf#page=7) (§4) makes only a cursory reference to securing model weights.} and how the large developer secures unreleased model weights from unauthorized modification or transfer by internal or external parties.

&nbsp;&nbsp;(8) [To the extent that the foundation model is controlled by the large developer,]{This acknowledges that critical incident monitoring and response will necessarily look different for open source developers than it looks for closed source developers. For instance, an open source developer cannot withdraw public access to a model in response to a critical incident, whereas a closed source developer can withdraw access by taking a model off their API.} the procedures the large developer will use to monitor critical safety incidents and the steps that a large developer would take to respond to a critical safety incident, including, but not limited to, whether the large developer has the ability to promptly shut down copies of foundation models owned and controlled by the large developer, who the large developer will notify, and the timeline on which the large developer would take these steps.

&nbsp;&nbsp;(9) The testing procedures that the large developer will use to [assess and manage]{Frontier developers' safety policies address risks from internal misuse to varying extents. It is unclear whether any developer is in compliance with this provision yet.
* Anthropic's [Responsible Scaling Policy](https://www-cdn.anthropic.com/f3b282f157017d08e36636bda1bf3bd4d9f23ee7.pdf) (§1) says that their deployment standards apply to both internal and external users. The Policy also mentions (§4.2) that Anthropic's model weight security standards are intended to prevent weight theft by employees. Anthropic does not explain how they assess risks from internal use of their models.
* OpenAI's [Preparedness Framework](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) (§3.2) clarifies that "significant" internally deployed systems are in scope for dangerous capability assessment. Further, OpenAI says (§4.4) that they will place safeguards on internal use of models that reach Critical capability thresholds.
* Google Deepmind's [Frontier Safety Framework](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/updating-the-frontier-safety-framework/Frontier%20Safety%20Framework%202.0.pdf) says nothing about assessing or managing risks from internal use.
* xAI has yet to publish an official safety policy. Their [draft safety policy](https://x.ai/documents/2025.02.20-RMF-Draft.pdf) (§3) says xAI will place safeguards on their models "prior to broad internal…deployment" but otherwise says nothing about risks from internal use.} a catastrophic risk or dangerous capability [resulting from the internal use]{That is, catastrophic risk resulting from a large developer using a model that has not yet been publicly deployed. Even before deployment, a model is vulnerable to theft by malicious outside actors and to catastrophic misuse by the developer's own staff. More speculatively, if a developer used a powerful misaligned model internally on sensitive engineering tasks, the model might strategically sabotage those tasks, causing a catastrophe at some later point. A misaligned model might also attempt to exfiltrate its own weights from the developer's computers before it is intentionally deployed. (Scientists have [already observed](https://www.anthropic.com/research/alignment-faking) models attempting to self-exfiltrate in controlled evaluations.)\\
The [California Report](https://www.cafrontieraigov.org/) (§2.4) found that advanced AI requires internal safeguards beyond those needed for other technologies. "Sophisticated AI systems, when sufficiently capable, may develop deceptive behaviors to achieve their objectives, including circumventing oversight mechanisms designed to ensure their safety. Because these risks are unique to AI compared to other technologies, oversight is critical for external outputs *as well as internal* testing and safety controls." (Emphasis added.)\\
For more analysis of risks from internal use of AI models, see "[AI models can be dangerous before public deployment](https://metr.org/blog/2025-01-17-ai-models-dangerous-before-public-deployment/)" by METR and "[AI Behind Closed Doors](https://www.apolloresearch.ai/research/ai-behind-closed-doors-a-primer-on-the-governance-of-internal-deployment)" by Apollo Research.} of its foundation models, including risks resulting from a foundation model circumventing oversight mechanisms, and the schedule, specified in days, by which the large developer will report these assessments pursuant to subdivision (d).

&nbsp;&nbsp;(10) How the developer determines when its foundation models are substantially [modified enough to conduct additional assessments]{AI developers will often make modifications to an AI system after its initial public deployment. For example, they might revise the [system prompt](https://docs.anthropic.com/en/release-notes/system-prompts), give the base model access to [additional tools](https://openai.com/index/introducing-chatgpt-search/), or raise the amount of compute the model is allowed to spend on [inference](https://www.nvidia.com/en-us/glossary/ai-inference/). All of these post-deployment updates can increase the model's dangerous capabilities or give it new dangerous propensities, potentially invalidating previous safety assessments.\\
Some frontier developers' existing safety policies acknowledge that post-deployment modifications may sometimes make it necessary to reassess an old model's safety.
* Anthropic's [Responsible Scaling Policy](https://www-cdn.anthropic.com/f3b282f157017d08e36636bda1bf3bd4d9f23ee7.pdf) (§3) says that they will rerun their dangerous capability assessments on an old model when "six months’ worth of finetuning and other capability elicitation methods have accumulated.  This is measured in calendar time, since we do not yet have a metric to estimate the impact of these improvements more precisely."
* OpenAI's [Preparedness Framework](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) (§3.2) says that they will re-measure the capabilities of an old model when there is a " significant change in the deployment conditions of an existing model (e.g., enabling finetuning, releasing weights, or significant new features) that makes the existing Capabilities Report or Safeguards Report no longer reasonably applicable," or when "incremental updates" cause "unexpectedly significant increases in capability."
* Google Deepmind's [Frontier Safety Framework](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/updating-the-frontier-safety-framework/Frontier%20Safety%20Framework%202.0.pdf) says that they will assess the capabilities of their frontier models "regularly," which presumably includes reassessment of old models. The Policy does not explicitly name any post-deployment modifications that would trigger new safety assessments.
* xAI has yet to publish an official safety policy. Their [draft safety policy](https://x.ai/documents/2025.02.20-RMF-Draft.pdf) mentions only pre-deployment safety testing, saying nothing about further post-deployment tests.} and publish a transparency report pursuant to subdivision (c).

(b) If a large developer makes a material modification to its safety and security protocol, the large developer shall clearly and conspicuously publish the modified protocol and a justification for that modification within 30 days.

(c) Before, or concurrently with, deploying a new foundation model or a substantially [modified version of an existing foundation model]{Subparagraph (a10) above leaves it up to developers to determine when an update to an existing model is substantial enough to require a new transparency report.\\ 
Measure 7.6 in the EU AI Act's [Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) requires a large AI developer to update a model report after deployment whenever they "have reasonable grounds to believe that the justification for why the systemic risks stemming from the model are acceptable… has been materially undermined." This requirement could trigger when a major post-deployment update is made to a model, when the model's "use and/or integrations" change materially, or when a serious incident "involving the model or a similar model" occurs. In general, the EU Code of Practice requires more active updates to transparency reports than SB 53 would require.\\
OpenAI has already [announced its intention](https://openai.com/global-affairs/eu-code-of-practice/) to sign the AI Act Code of Practice voluntarily. Meta has [refused](https://www.bloomberg.com/news/articles/2025-07-18/meta-says-it-won-t-sign-eu-s-ai-code-calling-it-overreach) to sign the Code, and other frontier AI developers have yet to weigh in.} that is covered by the large developer's safety and security protocol, a large developer shall clearly and conspicuously publish on its internet website a [transparency report]{The transparency report required by SB 53 is similar to a [model card](https://arxiv.org/abs/1810.03993), a report that most frontier AI developers voluntarily publish each time they release a new model. Anthropic, Google DeepMind, and OpenAI have consistently released model cards alongside their recent frontier models. Meta and xAI have published model cards for only some of their frontier models.\\
SB 53 transparency reports are also similar to the model reports required by the EU AI Act [Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/ai-code-practice) (Commitment 7). The EU CoP requires a developer to describe the risk identification and analysis they performed on their model, the developer's justification for believing the model is safe to deploy, and the results of any third-party evaluations performed on the model, all of which are also required in a transparency report.\\ 
The CoP goes beyond SB 53 in requiring developers to provide a high-level technical description of the model, including a specification (also known as a [spec](https://openai.com/index/introducing-the-model-spec/) or [constitution](https://www.anthropic.com/news/claudes-constitution)) and a copy of the system prompt. But SB 53 goes beyond the CoP in requiring transparency reports to be fully public, whereas model reports written under the EU CoP need only be submitted to the EU AI office.} containing both of the following:

&nbsp;&nbsp;(1) (A) The results of any risk assessment or risk mitigation assessment conducted by the large developer or a third party that contracts with a large developer pursuant to its safety and security protocol, why the information gathered by the large developer or third party leads to the stated results, and the steps taken to address any identified risks.

&nbsp;&nbsp;&nbsp;&nbsp;(B) A large developer shall disclose the [time and extent of predeployment access]{Following §3.1 of the [California Report](https://www.cafrontieraigov.org/), which also calls for developers to disclose the "time and depth of pre-deployment access provided" to third party evaluators.\\
Without this context, external observers cannot know how much weight to place on the results of a third party safety evaluation. AI developers [will sometimes give](https://metr.github.io/autonomy-evals-guide/openai-o3-report/#limitations) a third party evaluator access to a model too shortly before deployment or with too little information about how the model was trained for the evaluator to perform much elicitation on the model. This creates a gap between the capabilities measured by the evaluator and the theoretical ceiling on the capabilities that could be elicited in the field. The evaluator might not have observed some dangerous capability in the model, but that's only because they didn't sample it enough times or give it a sufficiently optimized prompt, not because the model's capabilities are inherently limited. \\
If a frontier developer discloses the time and extent of pre-deployment access granted to third-party evaluators, it will be easier for the external scientific community to estimate the size of any elicitation gap that might make the model more dangerous than it appears.} provided to any third party described in subparagraph (A), whether or not the third party was independent, and the nature of any constraints the large developer placed on the assessment or on the third party’s ability to disclose information about its assessment to the public or to government officials.

&nbsp;&nbsp;&nbsp;&nbsp;(C) Whether a catastrophic risk threshold or dangerous capability threshold has been attained for the foundation model and any actions taken as a result.

&nbsp;&nbsp;(2) (A) The reasoning behind the large developer’s decision to deploy the foundation model, the process by which the large developer arrived at that decision, and any limitations in the assessments that the large developer used to make that decision.

&nbsp;&nbsp;&nbsp;&nbsp;(B) A large developer may reuse an answer previously provided under subparagraph (A) if the rationale in question has not materially changed for the new deployment.

(d) A large developer shall clearly and conspicuously publish on its internet website any assessment of catastrophic risk or dangerous capabilities resulting from internal use of its foundation models pursuant to the schedule the developer specifies in its safety and security protocol.

(e) A large developer shall not make a [materially false or misleading statement]{Some false or misleading statements about catastrophic risk management might already be penalized under existing law.\\
California's [Unfair Competition Law](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?division=7.&chapter=5.&part=2.&lawCode=BPC) already forbids businesses from making "unfair, deceptive, untrue or misleading" claims about their products to consumers. If a large developer makes false or misleading statements to its users about catastrophic risks, it could thus expose itself to civil penalties under UCL. But UCL also has limitations. The fine for making a false or misleading statement is capped at $2,500, an extremely small figure compared to the losses a catastrophic risk would impose on society. And further, only private plaintiffs who have "suffered injury in fact" have standing to sue under UCL. This could make it practically challenging to sue a developer for making false or misleading statements before their model has actually caused a catastrophe.\\
Federal and state securities fraud laws could also ban certain false or misleading statements by developers. It is illegal under [SEC Rule 10b-5](https://www.govinfo.gov/content/pkg/CFR-2014-title17-vol4/pdf/CFR-2014-title17-vol4-sec240-10b-5.pdf) for a corporation "to make any untrue statement of a material fact or to omit to state a material fact necessary in order to make the statements made… not misleading… in connection with the purchase or sale of any security." Rule 10b-5 could be used against developers who make false or misleading claims to investors about their catastrophic risk management. But this legal strategy relies on an untested interpretation of materiality, and it would only apply to public companies or companies actively engaged in selling securities.\\
Overall, it seems likely that paragraph (e) would expand large developers' legal liability for false or misleading safety claims.} about catastrophic risk from its foundation models, its management of catastrophic risk, or its implementation of or compliance with its safety and security protocol.

(f) (1) When a large developer publishes documents to comply with this section, the large developer may make redactions to those documents that are necessary to protect the large developer’s trade secrets, the large developer’s cybersecurity, public safety, or the national security of the United States or to comply with any federal or state law.

&nbsp;&nbsp;(2) If a large developer redacts information in a document pursuant to this subdivision, the large developer shall describe the character and justification of the redaction in any published version of the document to the extent permitted by the concerns that justify redaction and shall retain the unredacted information for five years.

### 22757.13.

(a) The Attorney General shall [establish a mechanism]{This mechanism could be modeled on the mechanism that the California AG uses to [collect mandatory incident reports](https://oag.ca.gov/privacy/databreach/reporting) from companies that have suffered large data breaches.} to be used by a large developer or a member of the public to report a critical safety incident that includes all of the following:

&nbsp;&nbsp;(1) The date of the critical safety incident.

&nbsp;&nbsp;(2) The reasons the incident qualifies as a critical safety incident.

&nbsp;&nbsp;(3) A short and plain statement describing the critical safety incident.

(b) (1) Subject to paragraph (2), a large developer shall report any critical safety incident pertaining to one or more of its foundation models to the Attorney General within 15 days of discovering the critical safety incident.

&nbsp;&nbsp;(2) If a large developer discovers that a critical safety incident poses an imminent risk of death or serious physical injury, the large developer shall disclose that incident within 24 hours to an authority, including any law enforcement agency or public safety agency with jurisdiction, that is appropriate based on the nature of that incident and as required by law.

(c) The Attorney General shall review critical safety incident reports submitted by large developers and may review reports submitted by members of the public.

(d) The Attorney General may transmit reports of critical safety incidents, reports from employees made pursuant to Chapter 5.1 (commencing with Section 1107) of Part 3 of Division 2 of the Labor Code, and summaries of auditor reports required by Section 22757.14 to the Legislature, the Governor, the federal government, or appropriate state agencies.

(e) A report of a critical safety incident submitted to the Attorney General pursuant to this section, a employee report made pursuant to Chapter 5.1 (commencing with Section 1107) of Part 3 of Division 2 of the Labor Code, and a summary of an auditors report required by Section 22757.14 are exempt from the California Public Records Act (Division 10 (commencing with Section 7920.000) of Title 1 of the Government Code).

(f) (1) Beginning January 1, 2027, and annually thereafter, the Attorney General shall produce a report with anonymized and aggregated information about critical safety incidents, reports from employees made pursuant to Chapter 5.1 (commencing with Section 1107) of Part 3 of Division 2 of the Labor Code, and summaries of auditors reports required by Section 22757.14 that have been reviewed by the Attorney General since the preceding report.

&nbsp;&nbsp;(2) The Attorney General shall not include information in a report pursuant to this subdivision that would compromise the trade secrets or cybersecurity of a large developer, public safety, or the national security of the United States or that would be prohibited by any federal or state law.

&nbsp;&nbsp;(3) The Attorney General shall transmit a report pursuant to this subdivision to the Legislature, pursuant to Section 9795, and to the Governor.

### 22757.14.

(a) Beginning January 1, 2030, and at least annually thereafter, a large developer shall [retain an independent third-party auditor to produce a report]{New York's proposed [RAISE Act](https://www.nysenate.gov/legislation/bills/2025/A6453/amendment/A) (§1421.4) would also require every large AI developer to commission an annual audit of the developer's compliance with their own safety and security protocol.\\
There is precedent for this provision in the aviation and nuclear industries. Under Part 121 of the [Federal Aviation Regulation](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-G/part-121?toc=1), every airline in the US must write and implement a Safety Management System, a document laying out the airline's safety objectives and the measures it will take to achieve them. The airline must also commission regular independent audits to confirm that they are complying with their own Safety Management System.\\
The Nuclear Regulatory Commission requires every nuclear power plant operator to write a Quality Assurance Plan describing how they will ensure adherence to safety regulations. [CFR Title 10](https://www.nrc.gov/reading-rm/doc-collections/cfr/part050/part050-appb.html) says that the operator must also commission periodic audits to verify that they are in compliance with their quality assurance protocols.} assessing both of the following:

&nbsp;&nbsp;(1) Whether the large developer has substantially complied with its safety and security protocol and any instances of substantial noncompliance during the prior year.

&nbsp;&nbsp;(2) Any instances in which the large developers safety and security protocol has not been stated clearly enough to determine whether the large developer has complied.

(b) A large developer shall allow the third-party auditor access to all materials produced to comply with this chapter and any other materials reasonably necessary to perform the assessment required by this section.

(c) A large developer shall retain a report required by this section for five years.

(d) In conducting an audit for a large developer pursuant to this section, an auditor shall employ or contract one or more individuals with expertise in corporate compliance and one or more individuals with technical expertise in the safety of foundation models.

(e) Within 30 days after completing an audit, the auditor shall transmit to the Attorney General a high-level summary of the report required by this section that fairly presents, in all material respects, the outcome of the audit.

(f) An auditor shall not knowingly include a material misrepresentation or omit a material fact in a summary or report produced pursuant to this section

### 22757.15.

(a) On or before January 1, 2027, and annually thereafter, the Attorney General may adopt regulations to [update the definition of a “large developer”]{This allows the California Attorney General to adjust the training compute threshold for a person to count as a large developer upward or downward, or to replace it with a different kind of threshold altogether. For example, the compute threshold could be replaced with a cost threshold like the threshold used in New York's proposed [RAISE Act](https://www.nysenate.gov/legislation/bills/2025/A6453/amendment/A).} for the purposes of this chapter to ensure that it accurately reflects technological developments, scientific literature, and widely accepted national and international standards and [applies to well-resourced large developers at the frontier]{This paragraph allows the California Attorney General to redefine "large developer" at their own discretion to ensure that all well-resourced developers at the frontier of AI are covered. It does *not* allow the AG to redefine "large developer" in a way that would cover less well-resourced or behind-the-frontier developers. According to paragraph (c), the legislature would have to approve any proposed redefinition of "large developer" that covers startups or other small developers.} of artificial intelligence development.

(b) In developing regulations pursuant to this section, the Attorney General shall take into account all of the following:

&nbsp;&nbsp;(1) Similar thresholds used in international standards or federal law, guidance, or regulations for the management of catastrophic risk.

&nbsp;&nbsp;(2) Input from stakeholders, including academics, industry, the open-source community, and governmental entities.

&nbsp;&nbsp;(3) The extent to which a person will be able to determine, before beginning to train or deploy a foundation model, whether that person will be subject to the regulations as a large developer with an aim toward allowing earlier determinations if possible.

&nbsp;&nbsp;(4) The complexity of determining whether a person is covered, with an aim toward allowing simpler determinations if possible.

&nbsp;&nbsp;(5) The external verifiability of determining whether a person is covered, with an aim toward definitions that are verifiable by parties other than the large developer.

(c) If the Attorney General determines that less well-resourced developers, or developers significantly behind the frontier of artificial intelligence, may create substantial catastrophic risk, the Attorney General shall promptly submit a report to the Legislature, pursuant to Section 9795, with a proposal for managing this source of catastrophic risk but [shall not include those developers]{This protects small developers from possible regulatory overreach. It says that Attorney General cannot redefine "large developer" to include behind-the-frontier developers unless the California Legislature and the Governor both approve.} within the definition of “large developer” without authorization in subsequently enacted legislation.

### 22757.16.
(a) A large developer who violates this chapter shall be subject to a civil penalty subject to all of the following:

&nbsp;&nbsp;(1) (A) For an unknowing violation that does not create a material risk of death, serious physical injury, or a catastrophic risk, a large developer shall be subject to a civil penalty in an amount not to exceed ten thousand dollars ($10,000).

&nbsp;&nbsp;&nbsp;&nbsp;(B) (i) If the violation is a first violation subject to a civil penalty pursuant to subparagraph (A), a large developer shall be provided with a 30-day period to cure the violation after notification by the Attorney General. If the violation is cured within that period, a civil penalty shall not be imposed for that violation.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(ii) For the purposes of this subparagraph, a violation involving the missing or late publication or submission of a document is cured when the developer publishes or submits that document, even if the publication or submission occurs after the statutory deadline.

&nbsp;&nbsp;(2) For a knowing violation that does not create a material risk of death, serious physical injury, or a catastrophic risk or an unknowing violation that creates a material risk of death, serious physical injury, or a catastrophic risk, a large developer shall be subject to a civil penalty in an amount not to exceed one hundred thousand dollars ($100,000).

&nbsp;&nbsp;(3) For a knowing violation that creates a material risk of death, serious physical injury, or a catastrophic risk, a large developer shall be subject to a civil penalty in an amount not to exceed one million dollars ($1,000,000) for a violation that is the large developers first such violation and in an amount not exceeding ten million dollars ($10,000,000) for any subsequent violation.

(b) A violation of this chapter by an auditor shall be subject to a civil penalty in an amount not to exceed ten thousand dollars ($10,000).

(c) A civil penalty described in this section shall be recovered in a civil action brought only by the Attorney General.

## SECTION 3.
Section 11546.8 is added to the Government Code, to read:

### 11546.8. 

(a) There is hereby established within the Government Operations Agency a consortium that shall develop, pursuant to this section, a framework for the creation of a [public cloud computing cluster]{Several other governments have recently established, or are in the process of establishing, public AI compute clusters similar to CalCompute.\\
In early 2024, New York State launched [Empire AI](https://www.empireai.edu/), an initiative to promote "safe, equitable, and accessible AI research and development" at New York's public and private universities. Empire AI's first compute cluster, housed within SUNY Buffalo, is already online.\\
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

(g) The consortium shall, consistent with state constitutional law, consist of [14 members as follows]{Like New York's [Empire AI](https://www.empireai.edu/) initiative, CalCompute will be governed by a board representing academia and civil society. Compared to CalCompute's board, Empire AI's board gives more representation to universities and none to labor organizations.}:

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

## SECTION 6.
The Legislature finds and declares that Section 2 of this act, which adds Chapter 25.1 (commencing with Section 22757.10) to Division 8 of the Business and Professions Code, imposes a limitation on the public's right of access to the meetings of public bodies or the writings of public officials and agencies within the meaning of Section 3 of Article I of the California Constitution. Pursuant to that constitutional provision, the Legislature makes the following findings to demonstrate the interest protected by this limitation and the need for protecting that interest:

Information in critical safety incident reports, summaries of auditors reports, and reports from employees may contain information that could threaten public safety or compromise the response to an incident if disclosed to the public.